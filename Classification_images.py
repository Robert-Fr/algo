from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

dataset=load_digits()
x=dataset.data
y=dataset.target
train_x,test_x,train_y,test_y= train_test_split(x,y,test_size=0.1)
classifier=MLPClassifier(hidden_layer_sizes=(80,27),activation='identity',  solver='lbfgs')
classifier.fit(train_x,train_y)
test_y_pred = classifier.predict(test_x)
print("Exactitude :",accuracy_score(test_y,test_y_pred))