from sklearn.neural_network import MLPClassifier
x=[[0., 0.], [0., 1.], [1., 0.], [1.,1.]]
y_AND=[0,0,0,1]


classifier=MLPClassifier(hidden_layer_sizes=(),activation='identity',  solver='lbfgs')
classifier.fit(x,y_AND)
x_AND_test=[[1.,1.]]
print(classifier.predict(x_AND_test))

x_OR=[[0., 0.], [0., 1.], [1., 0.], [1.,1.]]
y_OR=[0,1,1,1]


classifier.fit(x,y_OR)
x_OR_test=[[1.,1.]]
print(classifier.predict(x_OR_test))

y_XOR=[0,1,1,0]

classifier.fit(x,y_XOR)
x_XOR_test=[[0.,1.]]
print(classifier.predict(x_XOR_test))

classifier_XOR=MLPClassifier(hidden_layer_sizes=(4,2),activation='identity',solver='lbfgs')
classifier_XOR.fit(x,y_XOR)
x_XOR_test=[[0.,1.]]
print(classifier_XOR.predict(x))

classifier_XOR_ameliorer=MLPClassifier(hidden_layer_sizes=(4,2),activation='tanh',solver='lbfgs')
classifier_XOR_ameliorer.fit(x,y_XOR)
print(classifier_XOR_ameliorer.predict(x))




