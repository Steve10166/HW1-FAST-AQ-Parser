# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    if not all(nuc in ALLOWED_NUC for nuc in seq):
        raise ValueError("Invalid DNA sequence.")

    transcribed_seq = "".join(TRANSCRIPTION_MAPPING[nuc] for nuc in seq)

    return transcribed_seq[::-1] if reverse else transcribed_seq

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # Hey this is my comment
    # Again!
    return transcribe(seq, reverse=True)