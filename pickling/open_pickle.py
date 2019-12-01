
import pickle

with open('dictionary.pkl', 'rb') as p:
    recovered_dict = pickle.load(p)

print(recovered_dict)

