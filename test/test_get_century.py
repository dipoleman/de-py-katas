from src.get_century.get_century import get_century

def test_get_century():
    assert get_century(2004) == '21st'
    assert get_century(1999) == '20th'
    assert get_century(1877) == "19th"
    assert get_century(10000) == "101st"
    assert get_century(1) == "1st"
    assert get_century(5234) == "53rd"
    assert get_century(7147) == "72nd"

   
 