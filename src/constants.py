BASE_CFG = {
    "S" : [["NP", "VP"]],
    "NP" : [["DT", "NN"], ["NN"]],
    "VP" : [["VB"], ["VB", "NN"], ["VBD"], ["VBD", "NN"], 
            ["VBG"], ["VDG", "NN"], ["VBN"], ["VBN", "NN"],
            ["VBP"], ["VBP", "NN"], ["VBZ"], ["VBZ", "NN"]
        ],      
    "PP" : [["IN", "NP"]],
    "DT" : ["the", "this", "that", "these", "those", "my", "your"],
    "IN" : ["on"],
}

# VB verb, base form take
# VBD verb, past tense took
# VBG verb, gerund/present participle taking
# VBN verb, past participle taken
# VBP verb, sing. present, non-3d take
# VBZ verb, 3rd person sing. present takes