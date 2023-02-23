import spacy

nlp = spacy.load("target/trained_model/model-best")
doc = nlp("It lays a certain theoretical foundation for giant magnetostrictive relay actuator being used in the fields of cutting with invariableness cutting force.\tCopy")

def print_all_info():
    for ent in doc.ents:
        print(f'{ent.text:<20}    {ent.label_:<20}')

if __name__ == "__main__":
    print('Starting')
    print_all_info()