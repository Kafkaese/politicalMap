from polimap.scraper import get_political_position

def test_get_political_position_aland_center():
    assert type(get_political_position('/wiki/%C3%85land_Centre')) == str