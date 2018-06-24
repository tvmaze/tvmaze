"""Parse data from TVMaze."""

import datetime


def parse_date(
        val: str,
) -> datetime.date:
    """
    Parse date from TVMaze API.

    :param val: A date string
    :return: A datetime.date object
    """
    fmt = '%Y-%m-%d'
    return datetime.datetime.strptime(val, fmt).date()
