        # cfg = "S -> NP VP \n \
        #     PP -> P NP \n \
        #     NP -> Det N | Det N PP | 'I' \n \
        #     VP -> V NP | VP PP \n \
        #     Det -> 'an' | 'my' \n \
        #     N -> 'elephant' | 'pajamas' \n \
        #     V -> 'shot' \n \
        #     P -> 'in'"

BASE_CFG = {
    "S" : [["NP", "VP"]],
    "NP" : [["DT", "NN"], ["NN"]],
    "VP" : [["VB"], ["VB", "NN"]],
    "PP" : [["IN", "NP"]],
    "DT" : ["the"],
    "NN" : ["dog", "cat", "tree"],
    "IN" : ["on"],
    "VB" : ["chased", "perched"]
}

# Infinite
# BASE_CFG = {
#     "S" : ["NP VP"],
#     "NP" : ["DT NN", "NP NN"],
#     "VP" : ["VB", "VB NN", "VP PP"],
#     "PP" : ["IN NP"],
#     "DT" : ["the"],
#     "NN" : ["dog", "cat", "tree"],
#     "IN" : ["on"],
#     "VB" : ["chased", "perched"]
# }

# VB verb, base form take
# VBD verb, past tense took
# VBG verb, gerund/present participle taking
# VBN verb, past participle taken
# VBP verb, sing. present, non-3d take
# VBZ verb, 3rd person sing. present takes