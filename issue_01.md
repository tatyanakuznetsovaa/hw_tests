```
python3 -m doctest -o NORMALIZE_WHITESPACE -v issues_01.py

Trying:
    encode('WORLD')
Expecting:
    '.-- --- .-. .-.. -..'
ok
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('sos')
Expecting:
    Traceback (most recent call last):
        ...
    KeyError: 's'
ok
Trying:
    encode('HELLO      WORLD')
Expecting:
    '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'
ok
1 items had no tests:
    issues_01
1 items passed all tests:
   4 tests in issues_01.test_coding_in_morze
4 tests in 2 items.
4 passed and 0 failed.
Test passed.