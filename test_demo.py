from demo import foo


def test_foo():
    assert 4 == foo(1, 3)


def test_foo_bad():
    assert 5 == foo(1, 3)
