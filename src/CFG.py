from collections import defaultdict
import random
import os

# TODO comment
class CFG(object):
    """
    Simple CFG implementation. Initial code adapted from Eli Bendersky. 
    """
    def __init__(self, filename : str):
        self.prod = defaultdict(list)
        self.read_from_file(filename)

    def read_from_file(self, filename : str):
        file = open(os.path.join("data", filename))
        for line in file.readlines():
            sides = line.split("->")
            self.read_prod(sides[0].strip(), sides[1])
        file.close()

    def read_prod(self, lhs, rhs):
        """ Add production to the grammar. 'rhs' can
            be several productions separated by '|'.
            Each production is a sequence of symbols
            separated by whitespace.

            Usage:
                grammar.add_prod('NT', 'VP PP')
                grammar.add_prod('Digit', '1|2|3|4')
        """
        prods = rhs.split('|')
        for prod in prods:
            self.prod[lhs].append(tuple(prod.split()))

    def add_prod(self, lhs, rhs):
        if lhs in self.prod:
            for element in rhs:
                self.prod[lhs].append((element,))
        else:
            self.prod.update({lhs : [(element) for element in rhs]})
        print(self.prod)

    def gen_random(self, symbol):
        """ Generate a random sentence from the
            grammar, starting with the given
            symbol.
        """
        sentence = ''

        # select one production of this symbol randomly
        rand_prod = random.choice(self.prod[symbol])

        for sym in rand_prod:
            # for non-terminals, recurse
            if sym in self.prod:
                sentence += self.gen_random(sym)
            else:
                sentence += sym + ' '

        return sentence
    
if __name__ == "__main__":
    print(os.getcwd())
    grammar = CFG("base.cfg")
    grammar.add_prod("N", ["muffin"])
    grammar.add_prod("NN", ["this", "is", "a test"])
    for i in range(5):
        print(grammar.gen_random("S"))
