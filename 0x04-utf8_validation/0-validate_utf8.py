#!/usr/bin/python3
""" function to validiate the encoding """


def validUTF8(data):
    """ write the condition here """
    try:
        intendeddata = [n & 255 for n in data]
        bytes(intendeddata).decode("UTF-8")
        return True
    except Exception:
        return False
