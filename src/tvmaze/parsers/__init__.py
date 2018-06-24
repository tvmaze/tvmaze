"""Parse data from TVMaze."""

import datetime
import typing

import pendulum


def parse_date(
        val: typing.Optional[str],
) -> typing.Optional[datetime.date]:
    """
    Parse date from TVMaze API.

    :param val: A date string
    :return: A datetime.date object
    """
    fmt = '%Y-%m-%d'
    try:
        return datetime.datetime.strptime(val, fmt).date()
    except TypeError:
        if val is not None:
            raise


def parse_datetime(
        val: str,
) -> datetime.datetime:
    """
    Parse datetime from TVMaze API.

    :param val: A datetime string with a UTC offset
    :return: An aware datetime.datetime object
    """
    return pendulum.parse(val)


def parse_duration(
        val: typing.Optional[int],
) -> typing.Optional[datetime.timedelta]:
    """
    Parse duration from TVMaze API.

    :param val: A duration in minutes
    :return: A datetime.timedelta object
    """
    try:
        return datetime.timedelta(minutes=val)
    except TypeError:
        if val is not None:
            raise


def parse_time(
        val: str,
) -> typing.Optional[datetime.time]:
    """
    Parse time from TVMaze API.

    :param val: A time string
    :return: A datetime.time object
    """
    fmt = '%H:%M'
    try:
        return datetime.datetime.strptime(val, fmt).time()
    except ValueError:
        if val != '':
            raise


def parse_timestamp(
        val: int,
) -> datetime.datetime:
    """
    Parse timestamp from TVMaze API.

    :param val: A timestamp in seconds since the Unix Epoch
    :return: An aware datetime.datetime object in UTC
    """
    return datetime.datetime.fromtimestamp(val, tz=datetime.timezone.utc)
