# PairWise Poetry Writer

![The PairWise website.](https://github.com/ncy-xing/M7-Poetry-Generator/blob/39db997ea6cf82003cb5baf35d2fc90926ac2c93/static/example.png)

## Description
This program takes in two words and writes a poem based on the two words.  

## Quickstart 
Requires Python 3. 

Clone the repository and start a virtual environment: 

`python3 -m venv M7_env`

`source M7_env/bin/activate`

`pip3 install -r requirements.txt`

Run the server with `python3 application.py` and open `http://localhost:8000/` in a browser. 


## Design

### Model design 

The generation model is based on my research with Prof. Abhilasha Kumar in the [lexicon lab](https://thelexiconlab.github.io/) at Bowdoin College. Specifically, it was inspired by the Connector word search task (Kumar et al., 2021). In this task, a person is given two different words and must find one word that describes them (e.g., we can describe the words "dog" and "cat" with the word "pet"). Since the basis of metaphor (and poetry) is finding connections between two elements, the Connector task would be a fitting method  to incorporate intelligence into the PairWise system. Per the evaluation of general intellect developed by Jordanous (2013), the system displays general intellect by organizing its processes to resemble human cognition in the Connector task. 

### Program design

The program design was inspired by the blackboard architecture employed by Misztal and Indurkhya (2014), who modeled human brain function as a set of collaborating experts on word generation, emotional intelligence, and poem making. The PairWise system employs three generators which can be considered experts in their define functionality: a word generator, a sentence generator, and a poem generator. Like in Misztal and Indurkhya's work, these experts adapt one another's output to create a final product. 

*Word Generation:* The vocabulary set is built on The Small World of Words (SWOW) word association data developed by De Deyne et al. (2019). This dataset models associations for 12000 words in a multidimensional vector space. To replicate the Connector task across these words, I adapted analysis code I wrote while analyzing Connector data from Kumar and Hawkins. Particularly, one baseline we compared participants against was how well their generated words fell into the theoretical “midpoint” of two words. This model approximates participant performance to an extent and can be considered a computerized version of the task. It could then be adapted to generate words directly. After computing the midpoint for two words, the word generator finds the 250 closest words to the midpoint. The number of generated word size was refined to produce an adequate number of verbs, nouns, etc. while still remaining close to the original two words. The words are then tokenized via nltk and delivered to the sentence generator.  

*Sentence Generation:* The sentence generator uses tagged words from the word generator and arranges them into structures with grammatical logic. Like in Misztal and Indurkhya's system, it uses context-free grammar (CFG). The CFG used by this system was developed from a simple english CFG from Gudivada and Rao (2018), adapted to match the tokenizations offered by the nltk library. Some prepositions and articles (such as "the" and "a") are included in the CFG by default.  

*Evaluation:* The sentence generator also contained an evaluation component which valued some level of coherency so it would be understandable to readers, i.e., a product based approach. Generated sentences were evaluated based on their grammatical correctness using [LanguageTool for python](https://pypi.org/project/language-tool-python/). Generated sentences are ordered based on the least number of grammatical errors detected per sentence. This is to mitigate for any incorrect tokenizations by nltk which would result in an unreadable sentence. The generator also uses LanguageTool to correct any grammatical errors it identifies. 

*Poem Generation: * The poem generator accepted sentences and selected a semi-random number of sentences, sectioned and dispersed into a semi-random number of stanzas. It selects sentences in the order given by the sentence generator.   

### Challenges and Limitations
How working on this system challenged you as a computer scientist.
Sentence generation + grammar
CFG is limited/hard (not weighted, no infinitely recursing CFGs allowed)
Matching verb conjugation

## References
- De Deyne, S., Navarro, D.J., Perfors, A. Brysbaert, M., & Storms, Gert. (2019). The “Small World of Words” english word association norms for over 12,000 cue words. Research Models, 51(987–1006). https://doi.org/10.3758/s13428-018-1115-7
- Gudivada, A., & Rao, D.L. (2018). A simplistic context-free grammar for english language. In Gudivada, V.N., & Rao, C.R. (Eds.), Handbook of Statistics (pp. 15-29). Elsevier. https://doi.org/10.1016/bs.host.2018.07.003
- Jordanous, A.K. (2013). Evaluating computational creativity: a standardised procedure for evaluating creative systems and its application. University of Sussex. Thesis. https://hdl.handle.net/10779/uos.23395574.v1
- Kumar, A.A., Steyvers, M. and Balota, D.A. (2021), Semantic Memory Search and Retrieval in a Novel Cooperative Word Game: A Comparison of Associative and Distributional Semantic Models. Cognitive Science, 45: e13053. https://doi.org/10.1111/cogs.13053
- Misztal, J., & Indurkhya, B. (2014). Poetry generation system with an emotional personality. In ICCC (pp. 72-81).

Semantic distance = SWOW dataset
Grammar (CFG) = https://www.nltk.org/howto/generate.html 
Emotional Personality System [CITE]
Title generation: Key phrases are extracted from the text to determine the theme of the poem, and also to set its sentiment. The key phrase that is found the most inspir- ing for the experts is used as the title and main theme of the poem.
Blackboard architecture = model of brain with diff experts: word generation, emotional intelligence expert, poem making (uses CFG for grammar), evaluating expert, novelty/control experts
[CITE] A simplistic CFG for English language
https://thelexiconlab.github.io/papers/connector_cogsci_2021.pdf
https://thelexiconlab.github.io/papers/connector_cogsci_2021.pdf 
