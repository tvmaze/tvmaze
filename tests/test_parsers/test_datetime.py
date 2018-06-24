"""Test parsing of dates, times, and durations."""

import datetime
import typing

import pytest

import tvmaze.parsers


PARSE_DATE_PARAMS = {
    'Unix Epoch': (
        '1970-01-01', datetime.date(year=1970, month=1, day=1),
    ),
    'Day before Unix Epoch': (
        '1969-12-31', datetime.date(year=1969, month=12, day=31),
    ),
    'Date not available': (
        None, None,
    ),
}


@pytest.mark.parametrize(
    'test_input,expected',
    PARSE_DATE_PARAMS.values(),
    ids=list(PARSE_DATE_PARAMS.keys()),
)
def test_parse_date(
        test_input: typing.Optional[str],
        expected: datetime.date,
):
    """
    Test parsing dates from TVMaze API.

    :param test_input: A sample date string or None
    :param expected: The expected datetime.date object
    """
    assert tvmaze.parsers.parse_date(test_input) == expected


PARSE_TIME_PARAMS = {
    'Midnight': (
        '0:00', datetime.time(hour=0, minute=0),
    ),
    'Midnight with leading zero': (
        '00:00', datetime.time(hour=0, minute=0),
    ),
    'AM with single-digit hour': (
        '1:00', datetime.time(hour=1, minute=0),
    ),
    'AM with leading zero': (
        '01:00', datetime.time(hour=1, minute=0),
    ),
    'PM': (
        '13:00', datetime.time(hour=13, minute=0),
    ),
    'Quarter-past': (
        '12:15', datetime.time(hour=12, minute=15),
    ),
    'Half-past': (
        '12:30', datetime.time(hour=12, minute=30),
    ),
    'Missing time': (
        '', None,
    ),
}


@pytest.mark.parametrize(
    'test_input,expected',
    PARSE_TIME_PARAMS.values(),
    ids=list(PARSE_TIME_PARAMS.keys()),
)
def test_parse_time(
        test_input: str,
        expected: datetime.time,
):
    """
    Test parsing times from TVMaze API.

    :param test_input: A sample time string
    :param expected: The expected datetime.time object
    """
    assert tvmaze.parsers.parse_time(test_input) == expected
