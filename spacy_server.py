import spacy
import numpy as np
nlp = spacy.load('en_core_web_sm')

# Load our .npy train and test data.
TEST_DATA = np.load("./dataset/TEST_DATA_np.npy", allow_pickle=True)
TRAIN_DATA = np.load("./dataset/TRAIN_DATA_np.npy", allow_pickle=True)

# Display basic information on our data.
