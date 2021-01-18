import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Sepideh Alassi lives in suburbs of Basel and works at DaSch Swiss that is located close to Basel Airport.")

for ent in doc.ents:
    print(ent.text, ent.label_)