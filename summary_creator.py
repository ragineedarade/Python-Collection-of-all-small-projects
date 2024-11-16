import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
text = """Amidst the serene countryside, where
the golden hues of dawn spill over the rolling hills,
lies a quaint village untouched by the rush of modern life. The air, crisp and filled with 
the earthy scent of dew-kissed grass, 
carries the harmonious chirping of birds welcoming
a new day. Narrow cobblestone paths wind through a tapestry of 
thatched cottages, their gardens bursting with vibrant blooms.
Here, time seems to slow, allowing
the residents to savor each moment,
whether it's the simple joy of a 
shared morning coffee or the satisfaction of
tending to their lush vegetable patches. """
stopwords = list(STOP_WORDS)
# print(stopwords)
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
# print(doc)
tokens = [ token.text for token in doc ]
print(tokens)
