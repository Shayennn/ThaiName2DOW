from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import dataset

dow = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

data = dataset.load()
x_train, x_test, y_train, y_test = train_test_split(
    data[0], data[1], test_size=0.3)

clf = GaussianNB()
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
score = accuracy_score(y_test, y_pred)

for test, pred in zip(y_test, y_pred):
    if test == 2:
        print('Real:', dow[test], 'Pred:', dow[pred])
    else:
        print('Real:', dow[test], '\tPred:', dow[pred])

print('Test Size:', len(y_test))
print('Train Size:', len(y_train))
print('Accuracy:', score)
