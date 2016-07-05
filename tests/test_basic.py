from rdtsc import rdtsc


def test_basic():
    start = rdtsc.get_cycles()
    end = rdtsc.get_cycles()
    assert isinstance(end, int)
    assert isinstance(start, int)
    assert end > start
