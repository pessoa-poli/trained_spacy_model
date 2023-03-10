import spacy
from spacy.tokens import Span, DocBin
from spacy.matcher import PhraseMatcher
import numpy as np
import time

"""
This program's only purpose is to build the doc_bins that will be used by spacy to train the model. The doc bins are special binaries used by spacy.
"""

# Load the small NLP pre-trained model
nlp = spacy.load('en_core_web_sm')

# Load our .npy TrainData and TestData.
TEST_DATA = np.load("./dataset/TEST_DATA_np.npy", allow_pickle=True)
TRAIN_DATA = np.load("./dataset/TRAIN_DATA_np.npy", allow_pickle=True)

def display_basic_information_on_data(data:np.ndarray, label:str):
    print(f'Printing {label} information.')
    print("\nData summary:\n", data)
    print("\nData shape:\n", data.shape)
    print(10*'#')
    print()

# Build DocBin - DocBin is a container that efficiently save and store Doc objects. It can be saved to disc as a Binary file. It's used a posteriori to train the model.

def print_entry_info(entry):
    phrase = entry[0]
    entities_list = entry[1]['entities'][0]   
    # Print the phrase
    print(phrase)
    # Print the entities list
    print(entities_list)
    print(10*'#')

def build_doc_bin(data, save_file_path, is_test_data=False):
    entities_dictionary = {}
    docs = [] # List of documents where all docs will be appended as we generate them
    for i,entry in enumerate(data):        
        phrase = entry[0]
        doc = nlp(phrase)
        doc.ents = []
        try:
            if (not is_test_data): # If it isn't TestData it is TrainData
                entity_markup_list = entry[1]['entities']

                # Example ot entry on TrainData:
                """['It lays a certain theoretical foundation for giant magnetostrictive relay actuator being used in the fields of cutting with invariableness cutting force.\tCopy'
                 {'entities': [(68, 82, 'Device')]}]"""
                
            else:
                entity_markup_list = entry[1] # Test data has a different format. Whereas the train data stores the entity_markup inside a dictionary, under the key 'entities', the TestData stores it simply in a list, which means we have to remove the key index.

                # Example of entry on TestData:
                """["Don't take our word for it, check the Water Survey of Canada's factual PostgreSQL."                
                list([(71, 81, 'Resource')])]"""

        except Exception as e:
            print('The following entry was problematic to deal with:')
            print(10*'#')
            print(entry)
            print(10*'#')
            print('entitie_markup error: '+ e)
        
        # Since I'm not sure if all phrases house examples of a single entity, I have to proccess each entity_markup as if it could be of a different entity.
        for entity_markup in entity_markup_list:            
            pattern = phrase[entity_markup[0]:entity_markup[1]]
            # build a matcher
            matcher = PhraseMatcher(nlp.vocab)
            label = entity_markup[2]
            if label in entities_dictionary.keys():
                entities_dictionary[label] += 1
            else:
                entities_dictionary[label] = 1
            matcher.add(label, list(nlp.pipe([pattern])))                        
            matches = matcher(doc)
            if len(matches) == 0:            
                continue       
            try:
                doc.ents = [Span(doc,match[1],match[2],label) for match in matches]
            except Exception as e:
                print_entry_info(entry)
                print('Error: ' + e)
                break
            docs.append(doc)    
    doc_bin = DocBin(docs=docs)
    doc_bin.to_disk(save_file_path)
    with open("./dictionary.py","a+") as f:
        f.write(f"{entities_dictionary}")
    print(f'Saved the DocBin to directory: {save_file_path:20}')

# Main program workflow
if __name__ == "__main__":   
    display_basic_information_on_data(TEST_DATA,'TEST_DATA')

    display_basic_information_on_data(TRAIN_DATA,'TRAIN_DATA')

    # print('Creating a DocBin for the TRAIN_DATA')
    start = time.time()
    build_doc_bin(data=TRAIN_DATA, save_file_path='./doc_bins/train_data.doc_bin.spacy')

    # print('Creating a DocBin for the TEST_DATA')
    build_doc_bin(data=TEST_DATA, save_file_path='./doc_bins/test_data.doc_bin.spacy', is_test_data=True)

    end = time.time()
    print(f"\nTime to generate DocBins: {round(end-start,5)} seconds.")