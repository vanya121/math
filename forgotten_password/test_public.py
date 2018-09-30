from forgotten_password import generate_passwords


def test_example():
    expected_output = [
        'are',
        'arered',
        'areredroses',
        'areroses',
        'arerosesred',
        'red',
        'redare',
        'redareroses',
        'redroses',
        'redrosesare',
        'roses',
        'rosesare',
        'rosesarered',
        'rosesred',
        'rosesredare'
    ]
    assert generate_passwords(['roses', 'are', 'red']) == expected_output
