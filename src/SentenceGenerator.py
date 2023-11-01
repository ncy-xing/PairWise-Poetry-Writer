"""
Nancy Xing
Assignment: CSCI 3725 M7
Date: 10-2023
"""
from typing import *
# from nltk.parse.generate import generate
# from nltk import CFG
# from constants import BASE_CFG

class SentenceGenerator():
    """
    SentenceGenerator builds a context-free grammar from given tagged words 
    to generate grammatical sentences. It may supplement the given tagged words
    to include words from its own template CFG, eg to include common stop words
    such as 'the'.  
    """

    def __init__(self, word_groups : Dict[str, List]) -> None:
        self.cfg = {}
        pass
    
    def cfg_to_string(self, word_groups : Dict[str, List]) -> str:
        cfg_string = ""
        for tag, transitions in word_groups.items():
            line = f"{tag} -> "
            line += ' | '.join([self.parse_transition_element(t) for t in transitions])
            line += "\n"
            cfg_string += line
        return cfg_string
    
    def parse_transition_element(self, element : List) -> str:
        if type(element) == str:
            return f"'{element}'"
        return ' '.join(e for e in element)
    
    if __name__ == "__main__":
        # cfg = "S -> NP VP \n \
        #     PP -> P NP \n \
        #     NP -> Det N | Det N PP | 'I' \n \
        #     VP -> V NP | VP PP \n \
        #     Det -> 'an' | 'my' \n \
        #     N -> 'elephant' | 'pajamas' \n \
        #     V -> 'shot' \n \
        #     P -> 'in'"
        # grammar = CFG.fromstring(cfg)

        
        #   :param depth: The maximal depth of the generated tree.
        # :param n: The maximum number of sentences to return.
        pass
        

        
    
    