"""
Nancy Xing
Assignment: CSCI 3725 M7
Date: 10-2023
"""
from typing import *
import pandas as pd
import numpy as np
import scipy
import os
import sys


class WordGenerator():
    """
    WordGenerator decodes embeddings from a given database of words and generates
    words from the database based on semantic distance from given inspiring words.
    """

    def __init__(self, data_file : str, vocab_file : str) -> None:
        """
        Initialize word embedding data.
        
        data_file -- name of csv word embedding data file stored in data folder. 
        vocab_file -- name of csv containing all words in same order as data file.
        """
        print("Initializing Word Generator...")
        self.data_file = data_file
        # TODO refactor 
        self.embeddings = pd.read_csv(os.path.join("data", data_file)).transpose().values
        self.vocab = list(pd.read_csv(os.path.join("data", vocab_file)).Word)
        print("Initialized.")
    
    def midpoint_scores(self, word1 : str, word2 : str, n_results : List[int]) -> List[str]: 
        """
        Computes the midpoint between two words. Finds and returns the words in the vocab set 
        with the lowest cosine distance from the midpoint.

        word1, word2 -- word pair
        n_results -- number of midpoint words to return 
        """
        # Retrieve word pair vectors 
        w1_vector = self.embeddings[self.vocab.index(word1)]
        w2_vector = self.embeddings[self.vocab.index(word2)]
        midpoint = (w1_vector + w2_vector)/2

        # Compute midpoint score and word distances from score
        midpoint = midpoint.reshape((1, self.embeddings.shape[1]))
        similarities = 1 - scipy.spatial.distance.cdist(midpoint, self.embeddings, 'cosine')

        # Find closest words
        sim_array = np.array(similarities)
        sim_array_sorted = np.argsort(-sim_array).flatten() # gives sorted indices
        sim_array = np.flip(np.sort(sim_array)).flatten()
        closest_words = np.array([self.vocab[i] for i in sim_array_sorted])
        return closest_words[:n_results]

    def __str__(self) -> str:
        """Returns string of location and size of generator's data source."""
        serialize = "WordGenerator" + f"\ndata source = '{self.data_file}'" + \
            f"\nsize = {len(self.embeddings)} words"
        return serialize
    