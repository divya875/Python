# -*- coding: utf-8 -*-
"""DL_ICP_1b.pynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12t9MFK-FTO8dag6z1o6s-rlFwxxaOVM4
"""

import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import seaborn as sns


# Importing the DATASET 
import pandas as pd
dataset = pd.read_csv("breast_Canc.csv")
classes = ['Benign', 'Malignant']

X = dataset.iloc[:, 2:32].values
y = dataset.iloc[:, 1].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder_X_1 = LabelEncoder()
y = labelencoder_X_1.fit_transform(y)
print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Model Creation
temp = Sequential()

#Adding Hidden Layers
temp.add(Dense(40, input_dim=30, activation='relu')) 
temp.add(Dense(60, input_dim=30, activation='relu'))
temp.add(Dense(20, input_dim=8, activation='relu')) 
temp.add(Dense(300, input_dim=8, activation='relu')) 



#Ourtput
temp.add(Dense(1, activation='sigmoid'))
temp.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
temp_fitted = temp.fit(X_train, y_train, epochs=100, verbose=0,
                                     initial_epoch=0)
print(temp.summary())
print(temp.evaluate(X_test, y_test, verbose=0))

"""# New Section"""