from sklearn.naive_bayes import BernoulliNB
import numpy as np
import pandas as pd

data = pd.read_csv("/Users/alexwang/Downloads/接单/nb.csv")
X = np.array(data)[:,0:5]
target = np.array(data)[:,5]

# Bernoulli native bayes model
clf = BernoulliNB()
clf_model = clf.fit(X,target)
# 2
print(clf_model.predict([[1,1,0,0,1]]))
# 3
print(clf.predict_proba([[1,0,1,0,1]]))

