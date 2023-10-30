"""
Nancy Xing
Assignment: CSCI 3725 M7
Date: 10-2023
"""
import pandas as pd
import os


class WordGenerator():
    """
    WordGenerator decodes embeddings from a given database of words and generates
    words from the database based on semantic distance from given inspiring words.
    """

    def __init__(self, data_file : str) -> None:
        """
        Initialize word embedding data.
        
        data_file -- name of csv word embedding data file stored in data folder. 
        """
        print("Initializing Word Generator...")
        self.data_file = data_file
        self.embeddings = pd.read_csv(os.path.join("data", data_file)).transpose().values
        print("Initialized.")
    
    def __str__(self) -> str:
        """Returns string of location and size of generator's data source."""
        serialize = "WordGenerator" + f"\ndata source = '{self.data_file}'" + \
            f"\nsize = {len(self.embeddings)} words"
        return serialize
    