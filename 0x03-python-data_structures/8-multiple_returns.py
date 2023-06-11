#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    first = sentence[0] if size else None
    return (size, first)
