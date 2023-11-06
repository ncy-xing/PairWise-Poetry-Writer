"""
Nancy Xing
Assignment: CSCI 3725 M7
Date: 10-2023
"""
from typing import *
from .constants import BASE_CFG, START_SYMBOL
from .CFG import CFG

class SentenceGenerator():
    """
    SentenceGenerator builds a context-free grammar from given tagged words 
    to generate grammatical, unpunctuated sentences.  
    """

    def __init__(self) -> None:
        """
        Initialize base CFG. Add given words from CFG and construct final grammar. 
        """
        print("Initializing Sentence generator...")
        self.cfg = CFG(BASE_CFG)
    
    def add_word_groups(self, word_groups : Dict[str, List]) -> None:
        for symbol, transitions in word_groups.items():
            self.cfg.add_prod(symbol, transitions)

    def generate_sentences(self, n : int) -> List[str]:
        result = []
        for i in range(n):
            result.append(self.cfg.gen_random(START_SYMBOL))
        return result
    
    def get_cfg(self) -> str:
        return str(self.cfg)
    
    if __name__ == "__main__":
        pass
        

        
    
    