"""
Nancy Xing
Assignment: CSCI 3725 M7
Date: 10-2023
"""
from src.WordGenerator import WordGenerator

if __name__ == '__main__':
    print("Started Generator")
    word_generator = WordGenerator("swow_associative_embeddings.csv")
    print(word_generator)