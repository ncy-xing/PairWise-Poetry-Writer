"""
Nancy Xing
Assignment: CSCI 3725 M7
Date: 11-2023
"""
import numpy
from .constants import *
import random
from statistics import mean

class PoemGenerator():
    """Generates a formatted poem from a given list of sentences."""

    def __init__(self) -> None:
        """Initialize empty list of sentences."""
        self.sentences = []
    
    def reset(self) -> None:
        """Clears the internal list of sentences"""
        self.sentences = []

    def add_sentences(self, sentences : str) -> None:
        """Add given sentences to internal list."""
        self.sentences += sentences

    def generate_poem(self) -> str:
        """Generates poem with a semi-random number of sentences and dimensions."""
        poem = ""
        # Generate poem length and dimensions
        sentences = self.sentences[:random.randint(MIN_SENTENCES, MAX_SENTENCES)]
        partition = random.randint(MIN_SENTENCE_PARTITION, MAX_SENTENCE_PARTITION)
        num_stanzas = random.randint(MIN_STANZA_LEN, MAX_STANZA_LEN)

        stanzas = numpy.array_split(numpy.array(sentences), num_stanzas)
        for stanza in stanzas: 
            for sentence in stanza:
                poem += self.partition_sentence(sentence, partition)
            poem += '\n'
        return poem
    
    def partition_sentence(self, sentence : str, n_partitions : int) -> str:
        """
        Splits a sentence by new lines into the given number of partitions.
        Returns the sentence itself if partitioning fails.
        """
        result = ""
        words = sentence.split(' ')
        partition = len(words) // n_partitions
        try:
            lines = numpy.array_split(numpy.array(words), partition)
        except Exception:
            return sentence
        for l in lines:
            result += ' '.join([word for word in l]) + '\n'
        return result

    
    