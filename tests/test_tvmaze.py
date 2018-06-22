"""Broad testing for tvmaze."""


def test_importing():
    """Test importing tvmaze."""
    import tvmaze
    assert tvmaze.__name__ == 'tvmaze'
