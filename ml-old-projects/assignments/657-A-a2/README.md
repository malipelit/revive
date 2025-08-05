# Assignment: Nonlinear Dimensionality Reduction and Classification

## Objective

To gain experience on the use of classification.

## Datasets

Since the datasets are very large, they won't be found in the repo.

### Dataset A
This data is the splice junctions on DNA sequences. The given data set includes 2200 samples with 57 features, in the matrix ’fea’. It is a binary class problem. The class labels are either +1 or -1, given in the vector ’gnd’. Parameter selection and classification tasks are conducted on this data set. (File: DataA.csv) 

### Dataset B
This data consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) petal and sepal length. The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width. (File: DataB.csv)

### Dataset C
Handwritten digits of 0, 1, 2, 3, and 4 (5 classes). This dataset contains 2066 samples with 784 features corresponding to a 28 x 28 gray-scale (0-255) image of the digit, arranged in column-wise. This data is used to illustrate the difference between feature extraction methods. (File: DataC.csv)

## Tasks

### 1. Nonlinear Dimensionality Reduction
    - Locally Linear Embedding (LLE)
    - ISOMAP
    - Naive Bayes Classifier
    - PCA and LDA

This task applies LLE and ISOMAP to Dataset C for nonlinear dimensionality reduction using 5 neighbors and projecting to 4 dimensions. It includes visualizing digit '3' images in 2D using LLE and ISOMAP to observe variation patterns. A Naive Bayes classifier is trained on the reduced data using repeated train-test splits, and average accuracy is compared with PCA and LDA to evaluate performance.

### 2. Binary Classification
    - k Nearest Neighbor (k-NN)
    - Support Vector Machine (SVM) with rbf kernel
    - Naive Bayes Classifier
    - Decision Tree
    - Performance metrics (accuracy, precision, recall, and F1-score)

This task uses Dataset A for binary classification with k-NN, SVM (RBF kernel), Naïve Bayes, and Decision Tree. After Z-score normalization, the data is split into 70% training and 30% testing. Parameters for k-NN and SVM are tuned using 5-fold cross-validation. Each classifier is run 20 times with different splits, and the average accuracy, precision, recall, and F1-score are reported and compared.

### 3. Multi-Class Classification
    - Support Vector Machine (SVM) with linear kernel
    - the “one-versus-all” and “one-versus-one” strategy
    - Performance metrics (accuracy, precision, recall, and F1-score)
    - Confusion Matrix
    - Decision Tree

This task uses Dataset B for multi-class classification with SVM and Decision Tree. SVM is applied using both one-vs-all and one-vs-one strategies with a linear kernel. The data is split 70% for training and 30% for testing, and results are reported with accuracy, precision, recall, F1-score, and a confusion matrix. The Decision Tree is also used, and its results are compared with SVM.

## Results

The results can be viewed on the report which is named as `Report.pdf`