import pytest

from db_utilities import test_conn, test_cursor, drop_all_tables
from venue import Venue
from orm import save
from decimal import Decimal


#@pytest.fixture()
def clean_tables():
    breakpoint()
    drop_all_tables(test_conn, test_cursor)
    yield
    drop_all_tables(test_conn, test_cursor)

#def test_save_venue(clean_tables):
def test_save_venue():
    venue = Venue()
    venue.__dict__ = {'likes': 12, 'name':'Taco Place', 'price': 1, 'foursquare_id': 'akjklsaj', 'rating': 3, 'menu_url': 'www.foo.com'}

    # fill in code here

    test_cursor.execute('SELECT * FROM venues;')
    venue = test_cursor.fetchone()
    assert venue[1:-1] == ('akjklsaj', 'Taco Place', 1, Decimal('3'), 12, 'www.foo.com')

def test_mass_assignment(clean_tables):
    venue = Venue(name = 'Lucky Star', price = 2)

    assert venue.name == 'Lucky Star'
    assert venue.price == 2

breakpoint()
clean_tables()
#test_save_venue()

