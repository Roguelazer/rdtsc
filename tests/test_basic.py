import six

import rdtsc


def test_basic():
    start = rdtsc.get_cycles()
    end = rdtsc.get_cycles()
    assert isinstance(end, six.integer_types)
    assert isinstance(start, six.integer_types)
    assert end > start
