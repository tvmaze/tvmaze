"""Test parsing of countries."""

import tvmaze.parsers


def pytest_generate_tests(metafunc):
    """Generate test cases from test class parameters."""
    params = metafunc.cls.params[metafunc.function.__name__]
    tests = list(params.values())
    names = sorted(tests[0])
    values = [
        [test[arg] for arg in names]
        for test in tests
    ]
    ids = list(params.keys())
    metafunc.parametrize(
        argnames=names,
        argvalues=values,
        ids=ids,
    )


class TestCountry:
    """Tested good."""

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

    def test_valid(
            self,
            argument: str,
            expected: str,
    ):
        """
        Test parsing countries from TVMaze API.

        :param argument: A sample country name string
        :param expected: The expected country code
        """
        result = tvmaze.parsers.parse_country(argument)
        assert result.alpha_2 == expected
