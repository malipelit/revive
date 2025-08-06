
# load dataset
from sklearn import datasets
dataset = datasets.load_iris() #sklearn bunch
feature_names = dataset.feature_names

# convert to dataframe
import pandas as pd
df = pd.DataFrame(data=dataset.data, columns=feature_names)
df["target"] = dataset.target
class_names = dataset.target_names
print(class_names)

# summarize dataset
print("Dim of dataset: ", df.shape)
print("\nPeek: ")
print(df.head(10))
print("\nStatistics: ")
print(df.describe())
print("Class ditribution: ")
print(df.groupby('target').size())

# plot data
from matplotlib import pyplot as plt
# df[feature_names].plot(kind="box", subplots=True, layout=(2,2), sharex=False, sharey=False)
# plt.show()
# df[feature_names].hist()
# plt.show()
# pd.plotting.scatter_matrix(df[feature_names])
# plt.show()

# split out data
from sklearn.model_selection import train_test_split
X = df[feature_names]
y = df["target"]
X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size=.2, random_state=1)

# models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
models = [
    (
        "LogReg", 
        LogisticRegression(solver="liblinear", multi_class="ovr")
    ),
    (
        "LDA",
        LinearDiscriminantAnalysis()
    ),
    (
        "kNN",
        KNeighborsClassifier()
    ),
    (
        "D3",
        DecisionTreeClassifier()
    ),
    (
        "NaiveBayes",
        GaussianNB()
    ),
    (
        "SVM",
        SVC(gamma="auto")
    )
]

# train and evaluate models
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring="accuracy")
    results.append(cv_results)
    names.append(name)
    print()

# compare models
plt.boxplot(results, labels=names)
plt.title("Model Comparison")
plt.show()

# prediction
model = SVC(gamma="auto")
model.fit(X_train, y_train)
predictions = model.predict(X_validation)

# evaluate predictions
from sklearn import metrics
print(metrics.accuracy_score(y_validation, predictions))
print(metrics.confusion_matrix(y_validation, predictions))
print(metrics.classification_report(y_validation, predictions))