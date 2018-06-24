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


PARSE_DATETIME_PARAMS = {
    'Unix Epoch': (
        '1970-01-01T00:00:00+00:00',
        datetime.datetime(
            1970, 1, 1, 0, 0, 0,
            tzinfo=datetime.timezone.utc,
        ),
    ),
    'One Second Before Unix Epoch': (
        '1969-12-31T23:59:59+00:00',
        datetime.datetime(
            1969, 12, 31, 23, 59, 59,
            tzinfo=datetime.timezone.utc,
        ),
    ),
}


@pytest.mark.parametrize(
    'test_input,expected',
    PARSE_DATETIME_PARAMS.values(),
    ids=list(PARSE_DATETIME_PARAMS.keys()),
)
def test_parse_datetime(
        test_input: str,
        expected: datetime.datetime,
):
    """
    Test parsing datetimes from TVMaze API.

    :param test_input: A sample time string
    :param expected: The expected aware datetime.datetime object
    """
    assert tvmaze.parsers.parse_datetime(test_input) == expected


PARSE_DURATION_PARAMS = {
    'Hour': (60, datetime.timedelta(minutes=60)),
    'Half Hour': (30, datetime.timedelta(minutes=30)),
}


@pytest.mark.parametrize(
    'test_input,expected',
    PARSE_DURATION_PARAMS.values(),
    ids=list(PARSE_DURATION_PARAMS.keys()),
)
def test_parse_duration(
        test_input: int,
        expected: datetime.timedelta,
):
    """
    Test parsing durations from TVMaze API.

    :param test_input: A duration in minutes
    :param expected: The expected datetime.timedelta object
    """
    assert tvmaze.parsers.parse_duration(test_input) == expected


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


PARSE_TIMESTAMP_PARAMS = {
    'Unix Epoch': (
        0,
        datetime.datetime(
            1970, 1, 1, 0, 0, 0,
            tzinfo=datetime.timezone.utc,
        ),
    ),
    'Y2K New years eve': (
        946684799,
        datetime.datetime(
            1999, 12, 31, 23, 59, 59,
            tzinfo=datetime.timezone.utc,
        ),
    ),
    'Y2K': (
        946684800,
        datetime.datetime(
            2000, 1, 1, 0, 0, 0,
            tzinfo=datetime.timezone.utc,
        ),
    ),
}


@pytest.mark.parametrize(
    'test_input,expected',
    PARSE_TIMESTAMP_PARAMS.values(),
    ids=list(PARSE_TIMESTAMP_PARAMS.keys()),
)
def test_parse_timestamp(
        test_input: int,
        expected: datetime.datetime,
):
    """
    Test parsing timestamps from TVMaze API.

    :param test_input: A timestamp in seconds since the Unix Epoch
    :param expected: The expected aware datetime.datetime object in UTC
    """
    assert tvmaze.parsers.parse_timestamp(test_input) == expected
