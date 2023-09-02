import pytest

from src.lengthen_date.lengthen_date import lengthen_date

def test_lengthen_date():
    expected = 'Tuesday 21st March 2017'
    result = lengthen_date('21.03.2017')
    assert result == expected

    expected = 'Wednesday 22nd March 2017'
    result = lengthen_date('22.03.2017')
    assert result == expected

    expected = 'Thursday 23rd March 2017'
    result = lengthen_date('23.03.2017')
    assert result == expected

    expected = 'Friday 24th March 2017'
    result = lengthen_date('24.03.2017')
    assert result == expected

    expected = 'Saturday 25th March 2017'
    result = lengthen_date('25.03.2017')
    assert result == expected

    expected = 'Thursday 2nd March 2017'
    result = lengthen_date('02.03.2017')
    assert result == expected

    expected = 'Friday 3rd March 2017'
    result = lengthen_date('03.03.2017')
    assert result == expected

    expected = 'Saturday 4th March 2017'
    result = lengthen_date('04.03.2017')
    assert result == expected

# def test_invalid_date_in_February_throws_error():
#     with pytest.raises(Exception) as e:
#         result = lengthen_date('31.02.2022')
#         expected = "day is out of range for month"
#         assert result == expected
        
# def test_invalid_date_format_throws_error():
#     with pytest.raises(Exception) as e:
#         result = lengthen_date('36.12.2022')
#         expected = "time data '36.12.2022' does not match format '%d.%m.%Y'"
#         assert result == expected
    
# def test_invalid_argument_data_type_throws_error():
#     with pytest.raises(Exception) as e:
#         result = lengthen_date(12112023)
#         expected = 'strptime() argument 1 must be str, not int'
#         assert result == expected