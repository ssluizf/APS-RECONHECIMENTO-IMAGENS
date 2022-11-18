import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

iris = load_iris()

df = pd.DataFrame(iris.data,columns=iris.feature_names)
df['target'] = iris.target

full = df.drop(['target'], axis='columns')
ref = df.target

full_train, full_test, ref_train, ref_test = train_test_split(full, ref, test_size=0.2, random_state=1)

knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(full_train, ref_train)

prediction = knn.predict(full_test)

print(classification_report(ref_test, prediction))

