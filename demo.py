"""
Nancy Xing
Assignment: CSCI 3725 M7
Date: 10-2023
"""
from src.WordGenerator import WordGenerator
from src.SentenceGenerator import SentenceGenerator
from src.PoemGenerator import PoemGenerator
from src.constants import N_GENERATED_SENTENCES, N_GENERATED_WORDS, \
    EMBEDDINGS, VOCAB
import sys

if __name__ == '__main__':
    """
    Demo script which walks through all steps of poetry processing. 

    Usage:
        python3 demo.py fire ice >> demo_output.txt
        python3 demo.py oil water >> demo_output.txt
    """
    n_results = 10
    if len(sys.argv) < 3:
        print("Usage: word1 word2 [num_results]")
        sys.exit()

    # Word generation
    print("Started Generator")
    word_generator = WordGenerator(EMBEDDINGS, VOCAB)

    w1 = sys.argv[1]
    w2 = sys.argv[2]
    groups = word_generator.generate_word_groups(w1, w2, N_GENERATED_WORDS)

    # Sentence Generation
    sentence_gen = SentenceGenerator()
    sentence_gen.add_word_groups(groups)
    print(sentence_gen.get_cfg())

    print("Generating sentences...")
    sentences = sentence_gen.generate_sentences(N_GENERATED_SENTENCES)
    print("Generated sentences: ")
    for i in sentences:
        print(i)
    
    # Poem generation
    print("Generating poem...")
    poem_gen = PoemGenerator()
    poem_gen.add_sentences(sentences)
    print("\nGenerated poem: ")
    print(poem_gen.generate_poem())
