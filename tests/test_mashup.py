"""TEST - Mashup
Test mashing up ideologies
"""

# # Project # #
from ideology_mashup.methods import mashup_one, mashup_ideologies


def test_mashup_one():
    prefix = "foo"
    name = "bar"
    
    expected = "Foo-Bar"
    result = mashup_one(prefix=prefix, name=name)

    assert result == expected


def test_mashup_ideologies(ideologies, mashed_ideologies):
    result = mashup_ideologies(ideologies)

    assert set(result) == mashed_ideologies
