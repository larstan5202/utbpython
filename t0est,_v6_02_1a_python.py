from v6_02_1a_python import Country

def test_country_name():
    se = Country("Sverige", 10.5)
    assert se.get_name() == "Sverige"

def test_country_population():
    se = Country("Sverige", 10.5)
    assert se.get_population() == 10.5