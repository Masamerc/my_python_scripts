import pickle

example_dict = {"name":['Masa', 'Victoria', 'Kenji', 'Takeshi'],
                 "age":[25, 28, 30, 23 ]}

with open('dictionary.pkl', 'wb') as p:
    pickle.dump(example_dict, p)

