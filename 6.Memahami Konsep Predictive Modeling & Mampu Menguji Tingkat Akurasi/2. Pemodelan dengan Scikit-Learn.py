#Features & Label
import pandas as pd
dataset = pd.read_csv('dataset.csv')
# removing the target column Revenue from dataset and assigning to X
X = dataset.drop(['Revenue'],axis=1)
# assigning the target column Revenue to y
y = dataset['Revenue']
# checking the shapes
print("Shape of X:", X.shape)
print("Shape of y:", y.shape)
#Training dan Test Dataset
from sklearn.model_selection import train_test_split
# splitting the X, and y
X_train, X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
# checking the shapes
print("Shape of X_train :", X_train.shape)
print("Shape of y_train :", y_train.shape)
print("Shape of X_test :", X_test.shape)
print("Shape of y_test :", y_test.shape)
#Training Model: Fit
print("\nTraining Model: Fit\n")
from sklearn.tree import DecisionTreeClassifier
# Call the classifier
model = DecisionTreeClassifier()
# Fit the classifier to the training data
model = model.fit(X_train,y_train)
#Training Model: Predict
print('\nTraining Model: Predict\n')
# Apply the classifier/model to the test data
y_pred = model.predict(X_test)
print(y_pred.shape)
#Evaluasi Model Performance - Part 2
print('\nEvaluasi Model Performance - Part 2\n')
from sklearn.metrics import confusion_matrix, classification_report

# evaluating the model
print('Training Accuracy :', model.score(X_train, y_train))
print('Testing Accuracy :', model.score(X_test, y_test))

# confusion matrix
print('\nConfusion matrix:')
cm=confusion_matrix(y_test, y_pred)
print(cm)

# classification report
print('\nClassification report:')
cr=classification_report(y_test, y_pred)
print(cr)