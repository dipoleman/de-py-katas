from src.create_counter.create_counter import create_counter

def test_create_counter_up_one_invocation():
    counter = create_counter(0)
    up = counter['up']
    assert up() == 1
    
def test_create_counter_up_two_invocations():
    counter = create_counter(0)
    up = counter['up']
    assert up() == 1
    assert up() == 2

def test_create_counter_down_one_invocation():
    counter = create_counter(0)
    down = counter['down']
    assert down() == -1

def test_create_counter_down_two_invocations():
    counter = create_counter(0)
    down = counter['down']
    assert down() == -1
    assert down() == -2

def test_create_counter_up_and_down():
    counter = create_counter(5)
    up = counter['up']
    down = counter['down']
    assert up() == 6
    assert up() == 7
    assert down() == 6
    assert down() == 5
    assert down() == 4
    assert down() == 3
    assert up() == 4

    
