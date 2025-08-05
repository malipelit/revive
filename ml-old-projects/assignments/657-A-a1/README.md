# Assignment: Data Cleaning and Dimensionality Reduction

## Objective

To study how to apply some of the methods discussed in class like Data Cleaning and Dimensionality Reduction on two datasets.

## Data Sets

### Dataset A
This is a time-series dataset which is collected from a set of motion sensors for wearable activity recognition. The data is given in time order, with 19000 samples and 81 features. Some missing values are denoted by Not Available (NA) and also some outliers are present. (File: DataA.csv)

### Dataset B
Handwritten digits of 0, 1, 2, 3, and 4 (5 classes). This dataset contains 2066 samples with 784 features corresponding to a 28 x 28 gray-scale (0-255) image of the digit, arranged in column-wise. (File: DataB.csv) 

## Tasks

### 1. Data cleaning and preprocessing 
    - Outliers, missing values
    - Min-max normalization
    - Z-score normalization

The task involves identifying and correcting issues in Dataset A using class-taught data cleaning techniques. It then requires applying min-max and z-score normalization methods. Finally, histograms of features 9 and 24 should be plotted and compared before and after normalization to observe changes in distribution.

### 2. Feature Extraction
    - Principal Component Analysis (PCA)
    - Naive Bayes Classifier
    - Linear Discriminany Analysis (LDA)

The task focuses on feature extraction for Dataset B using dimensionality reduction techniques. PCA is applied to compute eigenvectors and eigenvalues, followed by visualizing data using selected principal components and comparing class separability. A Naive Bayes classifier is used on datasets with varying PCA dimensions to analyze classification error against retained variance. LDA is also applied for comparison with PCA, and the effectiveness of PCA as the best linear transformation method with orthonormal bases is to be demonstrated.


## Results

The results can be viewed on the report which is named as `Report.pdf`