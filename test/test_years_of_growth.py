from src.years_of_growth.years_of_growth import years_of_growth

def test_years_of_growth():
    input = years_of_growth(1000, 2000, 2, 12) 
    expected = 25
    assert input == expected

def test_years_of_growth_2():
    input = years_of_growth(1000, 1500, 50, 0) 
    expected = 1
    assert input == expected

def test_years_of_growth_3():
    input = years_of_growth(1000, 2000, 0, 100) 
    expected = 10
    assert input == expected