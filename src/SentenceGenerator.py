"""
Nancy Xing
Assignment: CSCI 3725 M7
Date: 10-2023
"""
from typing import *
from nltk.parse.generate import generate
from nltk import CFG
from .constants import BASE_CFG

class SentenceGenerator():
    """
    SentenceGenerator builds a context-free grammar from given tagged words 
    to generate grammatical sentences. It may supplement the given tagged words
    to include words from its own template CFG, eg to include common stop words
    such as 'the'.  
    """

    def __init__(self, word_groups : Dict[str, List]) -> None:
        """
        Initialize base CFG. Add given words from CFG and construct final grammar. 
        """
        self.cfg = BASE_CFG
        # TODO merge given words into CFG 
        self.grammar_string = self.cfg_to_string(BASE_CFG)
        pass
    
    def cfg_to_string(self, word_groups : Dict[str, List]) -> str:
        # TODO comment
        cfg_string = ""
        for tag, transitions in word_groups.items():
            line = f"{tag} -> "
            line += ' | '.join([self.parse_transition_element(t) for t in transitions])
            line += "\n"
            cfg_string += line
        return cfg_string
    
    def parse_transition_element(self, element : List) -> str:
        # TODO comment
        if type(element) == str:
            return f"'{element}'"
        return ' '.join(e for e in element)
    
    def generate_sentences(self, n_results=5) -> List[str]:
        sentences = []
        grammar = CFG.fromstring(self.grammar_string)
        for s in generate(grammar, n=n_results):
            sentences.append(' '.join(s))
        return sentences
    
    if __name__ == "__main__":
        pass
        

        
    
    