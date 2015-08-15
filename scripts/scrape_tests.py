

def test_open_url():
    from doe_scrape import Scraper

    result = Scraper.open_url("http://www.imdb.com/name/nm0681250/?ref_=fn_al_nm_1")
    assert len(result) > 0
    try:
        Scraper.open_url("http://www.imdb.com/wholebunchofgarbage")
        assert False
    except:
        assert True

    print "A valid url. Look at you."


test_open_url()