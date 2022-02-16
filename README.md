# Project Details

This repo contain machine learning projects

## 1. Multiple Linear Regression Model
Using Multiple Linear Regression model to predict the consumption of fuel by a car.

The data set was downloaded from this website :- https://vincentarelbundock.github.io/Rdatasets/datasets.html

This project was done to implement my learnings about the machine learning algorithms.

![output](https://user-images.githubusercontent.com/90661230/150852731-bbd62fbb-3219-4ded-ba33-a41bac52d62e.png)


## 2. Logistic Regression

In statistics, the Logistic Regression model is a widely used statistical model which is primarily used for classification purposes. It means that given a set of observations, Logistic Regression algorithm helps us to classify these observations into two or more discrete classes. So, the target variable is discrete in nature.

![index](https://user-images.githubusercontent.com/90661230/152688077-0294ded5-65ee-4e7d-8f8b-ed354c65a605.png)

**Problem Statement**

In this project, I try to answer the question that whether or not an employee will quit a his/her job. I implement Logistic Regression with Python and Scikit-Learn.

To answer the question, I build a classifier to predict whether or not an employee will quit a his/her job by training a binary classification model using Logistic Regression. I have used the Rain in Australia dataset downloaded from the Kaggle website for this project.

The Python implementation is presented in the Jupyter notebook

**Result**

The logistic regression model accuracy score is  0.84 and 10-fold cross validation average accuracy: 0.837. So, the model does a very good job in predicting whether or not  an employee will quit a his/her job  The model shows no signs of overfitting.


## 3. Decision Tree Algorithm

Decision Tree algorithm belongs to the family of supervised learning algorithms. Unlike other supervised learning algorithms, the decision tree algorithm can be used for solving regression and classification problems too \The goal of using a Decision Tree is to create a training model that can use to predict the class or value of the target variable by learning simple decision rules inferred from prior data(training data).\In Decision Trees, for predicting a class label for a record we start from the root of the tree. We compare the values of the root attribute with the record’s attribute. On the basis of comparison, we follow the branch corresponding to that value and jump to the next node.

![dt0](https://user-images.githubusercontent.com/90661230/153706104-40f960d1-814e-435e-ad84-6f1b6cafb3b2.png)

**Problem Statement**

In this projecct, The popular Titanic dataset is used(Available on kagel). I try to classify weather or not a passager will survive the the crash./n  To do this, the Decision Tree Classifier was used.
The Python implementation is presented in the Jupyter notebook

**Result**

The Decision tree model accuracy score is  0.83 and 10-fold cross validation average accuracy: 0.79.So, the model does a very good job in predicting whether or not a passenger will survive or not.


## 3. Support Vector Machine Algorithm

Support Vector Machine or SVM is one of the most popular Supervised Learning algorithms, which is used for Classification as well as Regression problems. However, it is primarily used for Classification problems in Machine Learning.

The goal of the SVM algorithm is to create the best line or decision boundary that can segregate n-dimensional space into classes so that we can easily put the new data point in the correct category in the future. This best decision boundary is called a hyperplane

![svm](https://user-images.githubusercontent.com/90661230/154235807-f51c9506-3017-4369-9134-b2192507e71f.png)


Linear SVM: Linear SVM is used for linearly separable data, which means if a dataset can be classified into two classes by using a single straight line, then such data is termed as linearly separable data, and classifier is used called as Linear SVM classifier.
Non-linear SVM: Non-Linear SVM is used for non-linearly separated data, which means if a dataset cannot be classified by using a straight line, then such data is termed as non-linear data and classifier used is called as Non-linear SVM classifier

**Problem Statement**

In this projecct, The  dataset used is based on "Bank Marketing" UCI dataset (please check the description at: http://archive.ics.uci.edu/ml/datasets/Bank+Marketing).The data is enriched by the addition of five new social and economic features/attributes (national wide indicators from a ~10M population country), published by the Banco de Portugal and publicly available at: https://www.bportugal.pt/estatisticasweb.This dataset is almost identical to the one used in [Moro et al., 2014] (it does not include all attributes due to privacy concerns). 

I try to classify weather or not client will a subscribe to a term deposit?./n  To do this, I used the SVM classifer.
The Python implementation is presented in the Jupyter notebook


**Result**

The Decision tree model accuracy score is  0.8 and 10-fold cross validation average accuracy: 0.8.So, the model does a very good job in predicting whether or not a passenger will survive or not.

Refrence : [Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, In press, http://dx.doi.org/10.1016/j.dss.2014.03.001
