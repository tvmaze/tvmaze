"""Test parsing of countries."""

import pytest

import tvmaze.parsers

PARSE_COUNTRY_PARAMS = {
    'Afghanistan':
        ('Afghanistan', 'AF'),
    'Albania':
        ('Albania', 'AL'),
    'Argentina':
        ('Argentina', 'AR'),
    'Armenia':
        ('Armenia', 'AM'),
    'Australia':
        ('Australia', 'AU'),
    'Austria':
        ('Austria', 'AT'),
    'Azerbaijan':
        ('Azerbaijan', 'AZ'),
    'Belarus':
        ('Belarus', 'BY'),
    'Belgium':
        ('Belgium', 'BE'),
    'Bosnia and Herzegovina':
        ('Bosnia and Herzegovina', 'BA'),
    'Brazil':
        ('Brazil', 'BR'),
    'Bulgaria':
        ('Bulgaria', 'BG'),
    'Canada':
        ('Canada', 'CA'),
    'Chile':
        ('Chile', 'CL'),
    'China':
        ('China', 'CN'),
    'Colombia':
        ('Colombia', 'CO'),
    'Croatia':
        ('Croatia', 'HR'),
    'Cyprus':
        ('Cyprus', 'CY'),
    'Czech Republic':
        ('Czech Republic', 'CZ'),
    'Denmark':
        ('Denmark', 'DK'),
    'Estonia':
        ('Estonia', 'EE'),
    'Finland':
        ('Finland', 'FI'),
    'France':
        ('France', 'FR'),
    'French Polynesia':
        ('French Polynesia', 'PF'),
    'Georgia':
        ('Georgia', 'GE'),
    'Germany':
        ('Germany', 'DE'),
    'Greece':
        ('Greece', 'GR'),
    'Hong Kong':
        ('Hong Kong', 'HK'),
    'Hungary':
        ('Hungary', 'HU'),
    'Iceland':
        ('Iceland', 'IS'),
    'India':
        ('India', 'IN'),
    'Iran, Islamic Republic of':
        ('Iran, Islamic Republic of', 'IR'),
    'Iraq':
        ('Iraq', 'IQ'),
    'Ireland':
        ('Ireland', 'IE'),
    'Israel':
        ('Israel', 'IL'),
    'Italy':
        ('Italy', 'IT'),
    'Japan':
        ('Japan', 'JP'),
    'Kazakhstan':
        ('Kazakhstan', 'KZ'),
    "Korea, Democratic People's Republic of":
        ("Korea, Democratic People's Republic of", 'KP'),
    'Korea, Republic of':
        ('Korea, Republic of', 'KR'),
    'Latvia':
        ('Latvia', 'LV'),
    'Lebanon':
        ('Lebanon', 'LB'),
    'Lithuania':
        ('Lithuania', 'LT'),
    'Malaysia':
        ('Malaysia', 'MY'),
    'Maldives':
        ('Maldives', 'MV'),
    'Mexico':
        ('Mexico', 'MX'),
    'Netherlands':
        ('Netherlands', 'NL'),
    'New Zealand':
        ('New Zealand', 'NZ'),
    'Norway':
        ('Norway', 'NO'),
    'Pakistan':
        ('Pakistan', 'PK'),
    'Peru':
        ('Peru', 'PE'),
    'Philippines':
        ('Philippines', 'PH'),
    'Poland':
        ('Poland', 'PL'),
    'Portugal':
        ('Portugal', 'PT'),
    'Puerto Rico':
        ('Puerto Rico', 'PR'),
    'Romania':
        ('Romania', 'RO'),
    'Russian Federation':
        ('Russian Federation', 'RU'),
    'Saudi Arabia':
        ('Saudi Arabia', 'SA'),
    'Serbia':
        ('Serbia', 'RS'),
    'Singapore':
        ('Singapore', 'SG'),
    'Slovenia':
        ('Slovenia', 'SI'),
    'South Africa':
        ('South Africa', 'ZA'),
    'Spain':
        ('Spain', 'ES'),
    'Sweden':
        ('Sweden', 'SE'),
    'Switzerland':
        ('Switzerland', 'CH'),
    'Taiwan, Province of China':
        ('Taiwan, Province of China', 'TW'),
    'Thailand':
        ('Thailand', 'TH'),
    'Trinidad and Tobago':
        ('Trinidad and Tobago', 'TT'),
    'Turkey':
        ('Turkey', 'TR'),
    'Ukraine':
        ('Ukraine', 'UA'),
    'United Arab Emirates':
        ('United Arab Emirates', 'AE'),
    'United Kingdom':
        ('United Kingdom', 'GB'),
    'United States':
        ('United States', 'US'),
    'Venezuela, Bolivarian Republic of':
        ('Venezuela, Bolivarian Republic of', 'VE'),
}


@pytest.mark.parametrize(
    'test_input,expected',
    PARSE_COUNTRY_PARAMS.values(),
    ids=list(PARSE_COUNTRY_PARAMS.keys()),
)
def test_parse_date(
        test_input: str,
        expected: str,
):
    """
    Test parsing countries from TVMaze API.

    :param test_input: A sample country name string
    :param expected: The expected country code
    """
    result = tvmaze.parsers.parse_country(test_input)
    assert result.alpha_2 == expected
