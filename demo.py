"""
Nancy Xing
Assignment: CSCI 3725 M7
Date: 10-2023
"""
from src.WordGenerator import WordGenerator
from src.SentenceGenerator import SentenceGenerator
from src.constants import BASE_CFG
import sys

from nltk.parse.generate import generate
from nltk import CFG

# TODO refactor and move to other folder
if __name__ == '__main__':
    """
    Demo script which walks through all steps of poetry processing. 
    """
    n_results = 10
    if len(sys.argv) < 3:
        print("Usage: word1 word2 [num_results]")
        sys.exit()
    if len(sys.argv) == 4:
        n_results = int(sys.argv[3])

    # Word generation
    print("Started Generator")
    word_generator = WordGenerator("swow_associative_embeddings.csv", "vocab.csv")
    print(word_generator)

    w1 = sys.argv[1]
    w2 = sys.argv[2]
    groups = word_generator.generate_word_groups(w1, w2, n_results)
    for i in groups.items():
        print (i)

    # Sentence Generation
    sentence_generator = SentenceGenerator(groups)
    test = sentence_generator.generate_sentences(15)
    print(test)