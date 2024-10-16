# content of test_sample.py
def inc(x):
    return x + 1

def palindrome(s):
    """
    ceci est une fonction pour detecter les palaindromes !!!
    params:
    s:string
    """
    if s==s[::-1]:
        return True
    return False

def test_answer():
    assert inc(3) == 4

def test_palindrome():
    assert palindrome("kayak")==True