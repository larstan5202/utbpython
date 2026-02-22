from v6_02a_python import Animal, Dog, Cat, Rooster, sound_off

def test_dog_noise(capsys):
    d = Dog()
    d.make_noise()
    captured = capsys.readouterr()
    assert "Voff" in captured.out

def test_cat_noise(capsys):
    c = Cat()
    c.make_noise()
    captured = capsys.readouterr()
    assert "Mjau" in captured.out

def test_rooster_noise(capsys):
    h = Rooster()
    h.make_noise()
    captured = capsys.readouterr()
    assert "Kuckeliku" in captured.out

def test_sound_off(capsys):
    animals = [Dog(), Cat(), Rooster()]
    sound_off(animals)
    out = capsys.readouterr().out
    assert "Voff" in out
    assert "Mjau" in out
    assert "Kuckeliku" in out