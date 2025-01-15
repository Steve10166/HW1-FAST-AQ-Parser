# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    parser = FastaParser("data/test.fa")
    records = list(parser)
    assert len(records) > 0

    parser = FastaParser("tests/blank.fa")
    with pytest.raises(ValueError):
        list(parser)

    with pytest.raises(ValueError):
        parser = FastaParser("tests/bad.fa")
        list(parser)
    pass


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    parser = FastaParser("data/test.fa")
    records = list(parser)
    assert len(records) > 0

    parser = FastaParser("data/test.fq")
    records = list(parser)
    assert records[0][0] is None


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    parser = FastqParser("data/test.fq")
    records = list(parser)
    assert len(records) > 0

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    parser = FastqParser("data/test.fq")
    records = list(parser)
    assert len(records) > 0

    parser = FastqParser("data/test.fa")
    records = list(parser)
    assert records[0][0] is None
