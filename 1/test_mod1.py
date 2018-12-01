import mod1


def test_get_offsets():
    assert list(mod1.get_offsets(0, [1, -2, 3, 1])) == [1, -1, 2, 3]


def test_get_first_repeat():
    assert mod1.get_first_repeat(0, [1, -2, 3, 1]) == 2
