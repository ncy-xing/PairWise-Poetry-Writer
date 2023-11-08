"""
Nancy Xing
Assignment: CSCI 3725 M7
Date: 11-2023
"""
from typing import *
from .constants import BASE_CFG, START_SYMBOL
from .CFG import CFG
import language_tool_python 

class SentenceGenerator():
    """
    A sentence generator backed by context-free grammar from given tagged words 
    which generates grammatical, unpunctuated and uncapitalized sentences.  
    """

    def __init__(self) -> None:
        """Initialize base CFG."""
        print("Initializing Sentence generator...")
        self.cfg = CFG(BASE_CFG)
        self.lang_tool = language_tool_python.LanguageTool("en-US")
    
    def add_word_groups(self, word_groups : Dict[str, List]) -> None:
        """
        Add tagged words to the CFG
        
        word groups -- tagged words in format {tag : [words]}
        """
        for symbol, transitions in word_groups.items():
            self.cfg.add_prod(symbol, transitions)

    def generate_sentences(self, n : int) -> List[str]:
        """
        Generate sentences from the CFG and evaluate grammatical quality.
        
        returns: list of sentences in ascending order from the least to most
        initial grammatical errors. Tries to corrects any grammatical errors. 
        """
        sentences = []
        for i in range(n):
            sentences.append(self.cfg.gen_random(START_SYMBOL))
        scored_sentences = [self.eval_sentence(s) for s in sentences]
        scored_sentences.sort(key=lambda a: a[0])
        return [s[1] for s in scored_sentences]
    
    def eval_sentence(self, sentence : str) -> tuple[float, str]:
        """
        Evaluates the number of grammatical errors in a sentence and tries to
        correct the sentence. 

        returns: (score, corrected sentence)
        """
        # with language_tool_python.LanguageTool("en-US") as lang_tool:
            # matches = lang_tool.check(sentence)
        matches = self.lang_tool.check(sentence)
        return (len(matches), self.lang_tool.correct(sentence))
    
    def get_cfg(self) -> str:
        """Returns the internal CFG."""
        return str(self.cfg)

        

        
    
    