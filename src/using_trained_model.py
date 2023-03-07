import spacy

nlp = spacy.load("target/trained_model/model-best")
doc = nlp("It lays a certain theoretical foundation for giant magnetostrictive relay actuator being used in the fields of cutting with invariableness cutting force.\tCopy. monitoring software that detects nudity, drug use, and foul language and sends me live footage when it occurs.He's the repository of our common history, and by that right, grand patron of the Bicentennial.Don't take our word for it, check the Water Survey of Canada's factual PostgreSQL.")

def print_all_info():
    for ent in doc.ents:
        print(f'{ent.text:<20}    {ent.label_:<20}')

if __name__ == "__main__":
    print('Starting')
    print_all_info()