import spacy
nlp=spacy.load('en_core_web_md')

def NER(text):
    map = {}
    doc = nlp(text)
    for word in doc.ents:
        map[word.text] = word.label_

    return map

text = 'In 1793, Alexander Hamilton recruited Webster to move to New York City and become an editor for a Federalist Party newspaper.'
print(NER(text))