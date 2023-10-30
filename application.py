"""
Nancy Xing
Assignment: CSCI 3725 M7
Date: 10-2023
"""
from src.WordGenerator import WordGenerator
import sys

if __name__ == '__main__':
    # Test word generation
    if len(sys.argv) < 3:
        print("Usage: word1 word2 num_results")
        sys.exit()

    print("Started Generator")
    word_generator = WordGenerator("swow_associative_embeddings.csv", "vocab.csv")
    print(word_generator)

    w1 = sys.argv[1]
    w2 = sys.argv[2]
    closest_words = word_generator.generate_midpoint_words(w1, w2, 10)

    print(f"Midpoint words from '{w1}' and '{w2}': {closest_words}")
    print(f"Tagged words: {word_generator.tag_words(closest_words)}")
