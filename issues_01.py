from morse import encode


def test_coding_in_morze():
    """
    >>> encode('WORLD')
    '.-- --- .-. .-.. -..'
    >>> encode('SOS')
    '... --- ...'
    >>> encode('sos')
    Traceback (most recent call last):
        ...
    KeyError: 's'
    >>> encode('HELLO      WORLD')
    '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'
    >>> encode('123456L') # doctest: +SKIP
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
