from password import password_strength


def test_example1():
    assert password_strength('Anna12345') == 'weak'
