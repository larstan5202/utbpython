from my_functions import c_to_f, is_even

def test_c_to_negative():
    assert c_to_f(-40) == 40

def test_is_even_true():
    assert is_even(5) is True

def test_is_even_false():
    assert is_even(4) is True
