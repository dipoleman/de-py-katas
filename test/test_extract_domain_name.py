import pytest
from src.extract_domain_name.extract_domain_name import (extract_domain_name,BadInputError)

def test_returns_a_string():
    input = "https://www.reddit.com/"
    output = extract_domain_name(input)
    assert type(output) == str

def test_returns_a_domain_name_starting_with_https():
    input = "https://www.reddit.com/"
    output = extract_domain_name(input)
    expected = 'reddit.com'
    assert output == expected

def test_returns_a_domain_name_starting_with_http():
    input = "http://www.reddit.com/"
    output = extract_domain_name(input)
    expected = 'reddit.com'
    assert output == expected

def test_returns_a_domain_name_starting_with_no_www():
    input = "http://reddit.com/"
    output = extract_domain_name(input)
    expected = 'reddit.com'
    assert output == expected

def test_returns_a_domain_name_with_uk():
    input = "https://www.reddit.uk/"
    output = extract_domain_name(input)
    expected = 'reddit.uk'
    assert output == expected

def test_returns_domain_name_from_comples_query_url():
    input = "https://www.google.com/search?q=cats&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjO9Mrw2_v6AhXtTEEAHWYIBi8Q_AUoAXoECAIQAw&biw=1440&bih=764&dpr=2"
    output = extract_domain_name(input)
    expected = 'google.com'
    assert output == expected

def test_error_if_input_is_not_a_string_error():
    with pytest.raises(BadInputError, match="Invalid input: 7 is not a string"):
        extract_domain_name(7)

def test_error_if_no_domain_name_in_string():
    with pytest.raises(BadInputError, match="No domain name found in: nothing_to_see_here.com"):
        extract_domain_name('nothing_to_see_here.com')