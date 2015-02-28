#!/usr/bin/env python

import sys
import os
import subprocess

from setuptools import setup, find_packages

from distutils.command.build import build

if sys.platform == 'darwin':
    sofile = 'rdtsc.dylib'
elif sys.platform == 'win32':
    sofile = 'rdtsc.dll'
else:
    sofile = 'rdtsc.so.1'


class RTDSCBuild(build):
    def initialize_options(self):
        build.initialize_options(self)
        self.build_base = os.path.join(self.build_base, 'python')

    def run(self):
        subprocess.call(['cc', '-shared', '-o', sofile, '-fPIC', 'rdtsc.c'])
        build.run(self)


setup(
    name="rdtsc",
    version="0.1",
    author="James Brown",
    author_email="Roguelazer@gmail.com",
    url="https://github.com/Roguelazer/rdtsc",
    license="ISC",
    packages=find_packages(exclude=['tests']),
    cmdclass={'build': RTDSCBuild},
    data_files=[('lib', [sofile])],
    keywords=["performance"],
    description="Cycle timer wrapping the Intel X86 RTDSC instruction",
    test_suite="nose.collector",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
    ],
    zip_safe=False,
)
