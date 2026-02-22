from v6_01a_python import SafeStorage

def test_safe_storage():
    safe = SafeStorage()

    safe.put("Anakonda")
    x = safe.get()

    safe.put("Boaorm")
    y = safe.get()

    assert x == "Anakonda"
    assert y == "Boaorm"
