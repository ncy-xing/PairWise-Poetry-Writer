"""
Nancy Xing
Assignment: CSCI 3725 M7
Date: 10-2023
"""

from collections import defaultdict
import random
import os
from typing import List

class CFG(object):
    """
    Simple CFG implementation adapted from code by Eli Bendersky. 
    Note: Assumes no recursive structures in the input CFG. 
    """
    def __init__(self, filename : str) -> None:
        """Populate internal CFG with default transitions."""
        self.prod = defaultdict(list)
        self.read_from_file(filename)

    def read_from_file(self, filename : str) -> None:
        """Reads productions from given file."""
        file = open(os.path.join("data", filename))
        for line in file.readlines():
            self.read_prod(line)
        file.close()

    def read_prod(self, line : str) -> None:
        """ 
        Add production to the grammar given a line to parse. The right hand side 
        can be several productions separated by '|'. Each production is a sequence 
        of symbols separated by whitespace.
        
        Usage:
            grammar.read_prod('NT', 'VP PP')
            grammar.read_prod('Digit', '1|2|3|4')
        """
        sides = line.split("->")
        lhs = sides[0].strip()
        rhs = sides[1]

        prods = rhs.split('|')
        for prod in prods:
            self.prod[lhs].append(tuple(prod.split()))

    def add_prod(self, lhs : str, rhs : List) -> None:
        """Add production to the grammar given right and left hand sides."""
        if lhs in self.prod:
            for element in rhs:
                self.prod[lhs].append((element,))
        else:
            self.prod.update({lhs : [(element,) for element in rhs]})

    def gen_random(self, symbol : str) -> str:
        """ 
        Generate a random sentence from the grammar starting 
        with the given symbol.
        """
        sentence = ""
        if len(self.prod[symbol]) == 0:
            return ""
        # Select one production of this symbol randomly
        while True: 
            rand_prod = random.choice(self.prod[symbol])
            if(rand_prod in self.prod) and len(self.prod[rand_prod]) == 0: 
                del self.prod[rand_prod]
            else:
                break
            
        # For non-terminals, recurse
        for sym in rand_prod:
            if sym in self.prod:
                sentence += self.gen_random(sym)
            else:
                sentence += sym + ' '
        return sentence
    
    def __str__(self) -> str:
        """Serialize CFG."""
        serialize = ""
        for symbol, transitions in self.prod.items():
            serialize += f"{symbol} -> "
            lines = []
            for t in transitions:
                if len(t) == 1:
                    lines.append(t[0])
                else:
                    lines.append(' '.join(t))
            serialize += " | ".join([l for l in lines if len(l) != 0]) + "\n"
        return serialize
