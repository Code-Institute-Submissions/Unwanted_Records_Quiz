# To run tests, enter 'python3 unittests/test_input.py' into the terminal

# Test1 - testing python lowercase function

def test_lower_case(guess, answer):
    assert guess != answer, "{0} is not the same as {1}".format(guess, answer)
    assert guess.lower() != answer, "{0} is the same as {1}".format(guess, answer)
    assert guess.lower() == answer.lower(), "{0} is the same as {1}".format(guess, answer)

test_lower_case("derby county", "Derby County")

# Test2 - testing strip function

def test_strip(guess, answer):
    assert guess != answer, "{0} is not the same as {1}".format(guess, answer)
    assert guess.strip(' \t\n\r') == answer, "{0} is not the same as {1}".format(guess, answer)
    
test_strip("Duncan Ferguson ", "Duncan Ferguson")

# Test3 - testing lowercase and strip function together

def test_lower_strip(guess, answer):
    assert guess.lower() != answer.lower(), "{0} is the same as {1}".format(guess, answer)
    assert guess.strip(' \t\n\r') != answer, "{0} is not the same as {1}".format(guess, answer)
    assert guess.lower().strip(' \t\n\r') != answer, "{0} is not the same as {1}".format(guess, answer)
    assert guess.lower().strip(' \t\n\r') == answer.lower(), "{0} is not the same as {1}".format(guess, answer)
    
test_lower_strip(" gareth bale ", "Gareth Bale")

print("All tests passed")