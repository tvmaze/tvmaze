"""Test parsing of dates, times, and durations."""

import datetime

import pytest

import tvmaze.parsers


PARSE_DATE_PARAMS = {
    'Unix Epoch': (
        '1970-01-01', datetime.date(year=1970, month=1, day=1),
    ),
    'Day before Unix Epoch': (
        '1969-12-31', datetime.date(year=1969, month=12, day=31),
    ),
}


@pytest.mark.parametrize(
    'test_input,expected',
    PARSE_DATE_PARAMS.values(),
    ids=list(PARSE_DATE_PARAMS.keys()),
)
def test_parse_date(
        test_input: str,
        expected: datetime.date,
):
    """
    Test parsing dates from TVMaze API.

    :param test_input: A sample date string or None
    :param expected: The expected datetime.date object
    """
    assert tvmaze.parsers.parse_date(test_input) == expected
