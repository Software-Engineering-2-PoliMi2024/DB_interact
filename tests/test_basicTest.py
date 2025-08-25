import db_interact 

def test_Installation():
    db_interact.check_install()
    assert True

def test_NoDB():
    from db_interact import NoDB

    db = NoDB()
    with db:
        assert True

    assert True
    