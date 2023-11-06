from collections import defaultdict
import random
import os
from typing import List

# TODO comment
class CFG(object):
    """
    Simple CFG implementation. Initial code adapted from Eli Bendersky. 
    Assumes no recursive structures in the CFG. 
    """
    def __init__(self, filename : str) -> None:
        self.prod = defaultdict(list)
        self.read_from_file(filename)

    def read_from_file(self, filename : str) -> None:
        """
        Reads productions from given file. 
        """
        file = open(os.path.join("data", filename))
        for line in file.readlines():
            self.read_prod(line)
        file.close()

    def read_prod(self, line : str) -> None:
        """ 
        Add production to the grammar where the rhs is a string. 'rhs' can
        be several productions separated by '|'.
        Each production is a sequence of symbols
        separated by whitespace.

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
        """
        Add production to the grammar given rhs and lhs.
        """
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
        sentence = ''

        if len(self.prod[symbol]) == 0:
            return ""

        # select one production of this symbol randomly
        while True: 
            rand_prod = random.choice(self.prod[symbol])
            if(rand_prod in self.prod) and len(self.prod[rand_prod]) == 0: 
                del self.prod[rand_prod]
            else:
                break

        for sym in rand_prod:
            # for non-terminals, recurse
            if sym in self.prod:
                sentence += self.gen_random(sym)
            else:
                sentence += sym + ' '

        return sentence
    
    def __str__(self) -> str:
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
    
if __name__ == "__main__":
    print(os.getcwd())
    grammar = CFG("base.cfg")
    grammar.add_prod("N", ["muffin"])
    grammar.add_prod("NN", ["this", "is", "a test"])
    for i in range(5):
        print(grammar.gen_random("S"))
