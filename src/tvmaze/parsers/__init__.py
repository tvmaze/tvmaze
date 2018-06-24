"""Parse data from TVMaze."""

import datetime
import typing


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
