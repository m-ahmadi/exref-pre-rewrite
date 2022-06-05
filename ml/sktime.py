from sktime.classification.interval_based import TimeSeriesForestClassifier
from sktime.datasets import load_unit_test

X_train, y_train = load_unit_test(split='train', return_X_y=True)
X_test, y_test = load_unit_test(split='test', return_X_y=True)

clf = TimeSeriesForestClassifier(n_estimators=5)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)