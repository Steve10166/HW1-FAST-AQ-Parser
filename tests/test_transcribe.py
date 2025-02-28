# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    assert transcribe("ACTG") == "UGAC"
    assert transcribe("") == ""
    assert transcribe("T") == "A"
    assert transcribe("A") == "U"
    assert transcribe("ACTGAACCC") == "UGACUUGGG"
    pass


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    assert reverse_transcribe("ACTG") == "CAGU"
    assert reverse_transcribe("") == ""
    assert reverse_transcribe("T") == "A"
    assert reverse_transcribe("A") == "U"
    assert reverse_transcribe("ACTGAACCC") == "GGGUUCAGU"
    pass
