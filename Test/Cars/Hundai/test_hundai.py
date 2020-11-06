from pytest import mark


@mark.smoke
@mark.car
def test_sedan():
    assert True
