"""
Test parsing of data from the TVMaze API.

Tests are arranged into classes by the information being parsed.
Test cases are generated using pytest_generate_tests to convert the
classes params into a set of test cases per class test.
"""

import datetime
import typing

import pendulum
import pytest

import tvmaze.parsers


def pytest_generate_tests(metafunc):
    """Generate test cases from test class parameters."""
    test_name = metafunc.function.__name__
    test_cases = metafunc.cls.params[test_name]
    test_params = list(test_cases.values())
    arg_names = list(test_params[0].keys())
    values = [
        list(test.values())
        for test in test_params
    ]
    ids = list(test_cases.keys())
    metafunc.parametrize(
        argnames=arg_names,
        argvalues=values,
        ids=ids,
    )


class TestCountry:
    """Test parsing countries from TVMaze API."""

    params = {
        'test_valid': {
            'Afghanistan': {
                'argument': 'Afghanistan',
                'expected': 'AF',
            },
            'Albania': {
                'argument': 'Albania',
                'expected': 'AL',
            },
            'Argentina': {
                'argument': 'Argentina',
                'expected': 'AR',
            },
            'Armenia': {
                'argument': 'Armenia',
                'expected': 'AM',
            },
            'Australia': {
                'argument': 'Australia',
                'expected': 'AU',
            },
            'Austria': {
                'argument': 'Austria',
                'expected': 'AT',
            },
            'Azerbaijan': {
                'argument': 'Azerbaijan',
                'expected': 'AZ',
            },
            'Belarus': {
                'argument': 'Belarus',
                'expected': 'BY',
            },
            'Belgium': {
                'argument': 'Belgium',
                'expected': 'BE',
            },
            'Bosnia and Herzegovina': {
                'argument': 'Bosnia and Herzegovina',
                'expected': 'BA',
            },
            'Brazil': {
                'argument': 'Brazil',
                'expected': 'BR',
            },
            'Bulgaria': {
                'argument': 'Bulgaria',
                'expected': 'BG',
            },
            'Canada': {
                'argument': 'Canada',
                'expected': 'CA',
            },
            'Chile': {
                'argument': 'Chile',
                'expected': 'CL',
            },
            'China': {
                'argument': 'China',
                'expected': 'CN',
            },
            'Colombia': {
                'argument': 'Colombia',
                'expected': 'CO',
            },
            'Croatia': {
                'argument': 'Croatia',
                'expected': 'HR',
            },
            'Cyprus': {
                'argument': 'Cyprus',
                'expected': 'CY',
            },
            'Czech Republic': {
                'argument': 'Czech Republic',
                'expected': 'CZ',
            },
            'Denmark': {
                'argument': 'Denmark',
                'expected': 'DK',
            },
            'Estonia': {
                'argument': 'Estonia',
                'expected': 'EE',
            },
            'Finland': {
                'argument': 'Finland',
                'expected': 'FI',
            },
            'France': {
                'argument': 'France',
                'expected': 'FR',
            },
            'French Polynesia': {
                'argument': 'French Polynesia',
                'expected': 'PF',
            },
            'Georgia': {
                'argument': 'Georgia',
                'expected': 'GE',
            },
            'Germany': {
                'argument': 'Germany',
                'expected': 'DE',
            },
            'Greece': {
                'argument': 'Greece',
                'expected': 'GR',
            },
            'Hong Kong': {
                'argument': 'Hong Kong',
                'expected': 'HK',
            },
            'Hungary': {
                'argument': 'Hungary',
                'expected': 'HU',
            },
            'Iceland': {
                'argument': 'Iceland',
                'expected': 'IS',
            },
            'India': {
                'argument': 'India',
                'expected': 'IN',
            },
            'Iran, Islamic Republic of': {
                'argument': 'Iran, Islamic Republic of',
                'expected': 'IR',
            },
            'Iraq': {
                'argument': 'Iraq',
                'expected': 'IQ',
            },
            'Ireland': {
                'argument': 'Ireland',
                'expected': 'IE',
            },
            'Israel': {
                'argument': 'Israel',
                'expected': 'IL',
            },
            'Italy': {
                'argument': 'Italy',
                'expected': 'IT',
            },
            'Japan': {
                'argument': 'Japan',
                'expected': 'JP',
            },
            'Kazakhstan': {
                'argument': 'Kazakhstan',
                'expected': 'KZ',
            },
            "Korea, Democratic People's Republic of": {
                'argument': "Korea, Democratic People's Republic of",
                'expected': 'KP',
            },
            'Korea, Republic of': {
                'argument': 'Korea, Republic of',
                'expected': 'KR',
            },
            'Latvia': {
                'argument': 'Latvia',
                'expected': 'LV',
            },
            'Lebanon': {
                'argument': 'Lebanon',
                'expected': 'LB',
            },
            'Lithuania': {
                'argument': 'Lithuania',
                'expected': 'LT',
            },
            'Malaysia': {
                'argument': 'Malaysia',
                'expected': 'MY',
            },
            'Maldives': {
                'argument': 'Maldives',
                'expected': 'MV',
            },
            'Mexico': {
                'argument': 'Mexico',
                'expected': 'MX',
            },
            'Netherlands': {
                'argument': 'Netherlands',
                'expected': 'NL',
            },
            'New Zealand': {
                'argument': 'New Zealand',
                'expected': 'NZ',
            },
            'Norway': {
                'argument': 'Norway',
                'expected': 'NO',
            },
            'Pakistan': {
                'argument': 'Pakistan',
                'expected': 'PK',
            },
            'Peru': {
                'argument': 'Peru',
                'expected': 'PE',
            },
            'Philippines': {
                'argument': 'Philippines',
                'expected': 'PH',
            },
            'Poland': {
                'argument': 'Poland',
                'expected': 'PL',
            },
            'Portugal': {
                'argument': 'Portugal',
                'expected': 'PT',
            },
            'Puerto Rico': {
                'argument': 'Puerto Rico',
                'expected': 'PR',
            },
            'Romania': {
                'argument': 'Romania',
                'expected': 'RO',
            },
            'Russian Federation': {
                'argument': 'Russian Federation',
                'expected': 'RU',
            },
            'Saudi Arabia': {
                'argument': 'Saudi Arabia',
                'expected': 'SA',
            },
            'Serbia': {
                'argument': 'Serbia',
                'expected': 'RS',
            },
            'Singapore': {
                'argument': 'Singapore',
                'expected': 'SG',
            },
            'Slovenia': {
                'argument': 'Slovenia',
                'expected': 'SI',
            },
            'South Africa': {
                'argument': 'South Africa',
                'expected': 'ZA',
            },
            'Spain': {
                'argument': 'Spain',
                'expected': 'ES',
            },
            'Sweden': {
                'argument': 'Sweden',
                'expected': 'SE',
            },
            'Switzerland': {
                'argument': 'Switzerland',
                'expected': 'CH',
            },
            'Taiwan, Province of China': {
                'argument': 'Taiwan, Province of China',
                'expected': 'TW',
            },
            'Thailand': {
                'argument': 'Thailand',
                'expected': 'TH',
            },
            'Trinidad and Tobago': {
                'argument': 'Trinidad and Tobago',
                'expected': 'TT',
            },
            'Turkey': {
                'argument': 'Turkey',
                'expected': 'TR',
            },
            'Ukraine': {
                'argument': 'Ukraine',
                'expected': 'UA',
            },
            'United Arab Emirates': {
                'argument': 'United Arab Emirates',
                'expected': 'AE',
            },
            'United Kingdom': {
                'argument': 'United Kingdom',
                'expected': 'GB',
            },
            'United States': {
                'argument': 'United States',
                'expected': 'US',
            },
            'Venezuela, Bolivarian Republic of': {
                'argument': 'Venezuela, Bolivarian Republic of',
                'expected': 'VE',
            },
        },
    }

    @staticmethod
    def test_valid(
            argument: str,
            expected: str,
    ):
        """
        Test parsing valid countries.

        :param argument: A sample country name string
        :param expected: The expected country code
        """
        result = tvmaze.parsers.parse_country(argument)
        assert result.alpha_2 == expected


class TestDate:
    """Test parsing dates from TVMaze API."""

    params = {
        'test_valid': {
            'Unix Epoch': {
                'argument': '1970-01-01',
                'expected': datetime.date(year=1970, month=1, day=1),
            },
            'Day before Unix Epoch': {
                'argument': '1969-12-31',
                'expected': datetime.date(year=1969, month=12, day=31),
            },
            'Date not available': {
                'argument': None,
                'expected': None,
            },
        },
        'test_invalid': {
            'Do not pass int': {
                'argument': 1,
                'expected': TypeError,
            },
            'Do not pass datetime.date': {
                'argument': datetime.date(1970, 1, 1),
                'expected': TypeError,
            },
            'Do not pass datetime.datetime': {
                'argument': datetime.datetime(1970, 1, 1, 0, 0, 0),
                'expected': TypeError,
            },
        },
    }

    @staticmethod
    def test_valid(
            argument: typing.Optional[str],
            expected: datetime.date,
    ):
        """
        Test parsing valid dates.

        :param argument: A sample date string or None
        :param expected: The expected datetime.date object
        """
        assert tvmaze.parsers.parse_date(argument) == expected

    @staticmethod
    def test_invalid(
            argument: typing.Any,
            expected: Exception,
    ):
        """
        Test parsing invalid dates.

        :param argument: Invalid input such as an int
        :param expected: The exception expected
        """
        with pytest.raises(expected):
            tvmaze.parsers.parse_date(argument)


class TestDateTime:
    """Test parsing datetimes from TVMaze API."""

    params = {
        'test_valid': {
            'Unix Epoch': {
                'argument': '1970-01-01T00:00:00+00:00',
                'expected': datetime.datetime(
                    1970, 1, 1, 0, 0, 0,
                    tzinfo=datetime.timezone.utc,
                ),
            },
            'One Second Before Unix Epoch': {
                'argument': '1969-12-31T23:59:59+00:00',
                'expected': datetime.datetime(
                    1969, 12, 31, 23, 59, 59,
                    tzinfo=datetime.timezone.utc,
                ),
            },
        },
    }

    @staticmethod
    def test_valid(
            argument: str,
            expected: datetime.datetime,
    ):
        """
        Test parsing valid datetimes.

        :param argument: A sample time string
        :param expected: The expected aware datetime.datetime object
        """
        assert tvmaze.parsers.parse_datetime(argument) == expected


class TestDuration:
    """Test parsing durations from TVMaze API."""

    params = {
        'test_valid': {
            'Hour': {
                'argument': 60,
                'expected': datetime.timedelta(minutes=60),
            },
            'Half Hour': {
                'argument': 30,
                'expected': datetime.timedelta(minutes=30),
            },
            'None': {
                'argument': None,
                'expected': None,
            },
        },
        'test_invalid': {
            'Do not pass str': {
                'argument': '1',
                'expected': TypeError,
            },
            'Do not pass datetime.timedelta': {
                'argument': datetime.timedelta(minutes=1),
                'expected': TypeError,
            },
        },
    }

    @staticmethod
    def test_valid(
            argument: int,
            expected: datetime.timedelta,
    ):
        """
        Test parsing valid durations.

        :param argument: A duration in minutes
        :param expected: The expected datetime.timedelta object
        """
        assert tvmaze.parsers.parse_duration(argument) == expected

    @staticmethod
    def test_invalid(
            argument: typing.Any,
            expected: Exception,
    ):
        """
        Test parsing invalid durations.

        :param argument: An invalid input such as a str
        :param expected: The exception expected
        """
        with pytest.raises(expected):
            tvmaze.parsers.parse_duration(argument)


class TestTime:
    """Test parsing times from TVMaze API."""

    params = {
        'test_valid': {
            'Midnight': {
                'argument': '0:00',
                'expected': datetime.time(hour=0, minute=0),
            },
            'Midnight with leading zero': {
                'argument': '00:00',
                'expected': datetime.time(hour=0, minute=0),
            },
            'AM with single-digit hour': {
                'argument': '1:00',
                'expected': datetime.time(hour=1, minute=0),
            },
            'AM with leading zero': {
                'argument': '01:00',
                'expected': datetime.time(hour=1, minute=0),
            },
            'PM': {
                'argument': '13:00',
                'expected': datetime.time(hour=13, minute=0),
            },
            'Quarter-past': {
                'argument': '12:15',
                'expected': datetime.time(hour=12, minute=15),
            },
            'Half-past': {
                'argument': '12:30',
                'expected': datetime.time(hour=12, minute=30),
            },
            'Missing time': {
                'argument': '',
                'expected': None,
            },
        }, 'test_invalid': {
            'Invalid format': {
                'argument': '12:15:01',
                'expected': ValueError,
            },
            'Do not pass datetime.time': {
                'argument': datetime.time(0, 0, 0),
                'expected': TypeError,
            },
        },
    }

    @staticmethod
    def test_valid(
            argument: str,
            expected: datetime.time,
    ):
        """
        Test parsing valid times.

        :param argument: A sample time string
        :param expected: The expected datetime.time object
        """
        assert tvmaze.parsers.parse_time(argument) == expected

    @staticmethod
    def test_invalid(
            argument: typing.Any,
            expected: Exception,
    ):
        """
        Test parsing invalid times.

        :param argument: An invalid input such as an int or incorrect format
        :param expected: The exception expected
        """
        with pytest.raises(expected):
            tvmaze.parsers.parse_time(argument)


class TestTimeStamp:
    """Test parsing timestamps from TVMaze API."""

    params = {
        'test_valid': {
            'Unix Epoch': {
                'argument': 0,
                'expected': datetime.datetime(
                    1970, 1, 1, 0, 0, 0,
                    tzinfo=datetime.timezone.utc,
                ),
            },
            'Y2K New years eve': {
                'argument': 946684799,
                'expected': datetime.datetime(
                    1999, 12, 31, 23, 59, 59,
                    tzinfo=datetime.timezone.utc,
                ),
            },
            'Y2K': {
                'argument': 946684800,
                'expected': datetime.datetime(
                    2000, 1, 1, 0, 0, 0,
                    tzinfo=datetime.timezone.utc,
                ),
            },
        },
    }

    @staticmethod
    def test_valid(
            argument: int,
            expected: datetime.datetime,
    ):
        """
        Test parsing valid timestamps.

        :param argument: A timestamp in seconds since the Unix Epoch
        :param expected: The expected aware datetime.datetime object in UTC
        """
        assert tvmaze.parsers.parse_timestamp(argument) == expected


class TestTimeZone:
    """Test parsing timezones from TVMaze API."""

    params = {
        'test_valid': {
            'America/New_York': {
                'argument': 'America/New_York',
                'expected': pendulum.timezone('America/New_York'),
            },
            'Europe/London': {
                'argument': 'Europe/London',
                'expected': pendulum.timezone('Europe/London'),
            },
            'Europe/Stockholm': {
                'argument': 'Europe/Stockholm',
                'expected': pendulum.timezone('Europe/Stockholm'),
            },
            'Asia/Tokyo': {
                'argument': 'Asia/Tokyo',
                'expected': pendulum.timezone('Asia/Tokyo'),
            },
        },
    }

    @staticmethod
    def test_valid(
            argument: str,
            expected: datetime.tzinfo,
    ):
        """
        Test parsing valid timezones.

        :param argument: A sample timezone string
        :param expected: The expected timezone
        """
        assert tvmaze.parsers.parse_timezone(argument) == expected
