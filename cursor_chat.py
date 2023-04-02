import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import random
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers

import json
try:
    with open('confess.json') as file:
        data = json.load(file)
except FileNotFoundError as e:
    print("The program failed to read the confess file.")

words = []
labels = []
docs_x = []
docs_y = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent['tag'])

    if intent['tag'] not in labels:
        labels.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words if w != '?']
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

training = np.array(training)
output = np.array(output)

model = keras.Sequential(
    [
        layers.Dense(8, input_shape=(len(training[0]),)),
        layers.Dense(8),
        layers.Dense(len(output[0]), activation="softmax"),
    ]
)
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
try:
    model.fit(training, output, epochs=1000, batch_size=8)
except ValueError as e:
    print(e)

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)

def chat(inp):
    #print("Start talking with the bot (type quit to stop)!")
    while True:
        if inp.lower()=="quit":
            break

        results = model.predict(np.array([bag_of_words(inp, words)]))
        results_index = np.argmax(results)
        tag = labels[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        return(random.choice(responses))
