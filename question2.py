import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score,f1_score
from sklearn.inspection import DecisionBoundaryDisplay
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
# Importing necessary libraries
# Importing the csv files used for testing and training
testing= pd.read_csv('TestingDataMulti.csv', header=None)
training= pd.read_csv('TrainingDataMulti.csv', header=None)
# Declaring the random forest model
randomf = RandomForestClassifier()
# Getting the data ready for fitting, using the 128 features for training and the last column 'marker' for the testing and training
X = training.iloc[:,:-1]
y = training.iloc[:,-1]
# Declaring the variables for testing and training using an 80-20 split
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=.2, random_state=21)
randomf.fit(X_train, y_train)
y_prediction = randomf.predict(X_test)
# Predicting using the X_test variable

accuracy = accuracy_score(y_test, y_prediction)
print("Accuracy:", accuracy)
# Checking and printing the accuracy of our predictions using the testing y_test variable

label = randomf.predict(testing)
# To find the predicted values by using the testing data
result = pd.DataFrame(label, columns=['PredLabel'])
# Saving the predictions
testing['PredLabel'] = result["PredLabel"].tolist()
testing.to_csv("TestingResultsMulti.csv", index=False)