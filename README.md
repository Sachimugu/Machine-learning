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

![dc](https://user-images.githubusercontent.com/90661230/154813255-19b38840-3ea3-4ec3-aca4-cf93a42893b0.png)

**Problem Statement**

In this projecct, The popular Titanic dataset is used(Available on kagel). I try to classify weather or not a passager will survive the the crash./n  To do this, the Decision Tree Classifier was used.
The Python implementation is presented in the Jupyter notebook

**Result**

The Decision tree model accuracy score is  0.83 and 10-fold cross validation average accuracy: 0.79.So, the model does a very good job in predicting whether or not a passenger will survive or not.


## 4. Support Vector Machine Algorithm

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



## 5. Random Forest.
Random forest classifiers fall under the broad umbrella of ensemble-based learning methods. They are simple to implement, fast in operation, and have proven to be extremely successful in a variety of domains. The key principle underlying the random forest approach comprises the construction of many “simple” decision trees in the training stage and the majority vote (mode) across them in the classification stage. Among other benefits, this voting strategy has the effect of correcting for the undesirable property of decision trees to overfit training data.

![rf](https://user-images.githubusercontent.com/90661230/154436124-4bc58163-47bf-4819-871e-242128bb659a.png)

Random Forest was efficiently used predict the disease of a human, based on the symptoms that he/she posses.
Steps invovled were: Gathering of data at <a href='https://www.kaggle.com/kaushil268/disease-prediction-using-machine-learning'>kagel</a>, Cleaning the Data, Model Building, and Evaluation



## 6. Naïve Bayes.

Naïve Bayes is a probabilistic machine learning algorithm based on the Bayes Theorem, used in a wide variety of classification tasks.It has been successfully used for many purposes, but it works particularly well with natural language processing (NLP) problems.

![bayes](https://user-images.githubusercontent.com/90661230/154813113-e3d32c83-4d4a-4bbf-ab55-376898d9b204.png)

Bayes’ Theorem is a simple mathematical formula used for calculating conditional probabilities.
Conditional probability is the probability of an event happening, given that it has some relationship to one or more other events. For example, your probability of getting a parking space is connected to the time of day you park, where you park, and what conventions are going on at any time. Bayes’ theorem is slightly more nuanced. In a nutshell, it gives you the actual probability of an event given information about tests.

**Approach**

 In these project, I worked on the Email Spam Detection dataset here to classify emails if there are spam or not. Approach to the problem involved:
 1. Data cleaning
 2. Data visualisation
 3. NLP
 4. vectorization
 4. Model training
 5. Model evalution 

**Result**

Naïve Bayes did well with the dataset with an acurracy score of 99%


# 7. K-means-Clustering.
K-means clustering is one of the simplest and popular unsupervised machine learning algorithms.A cluster refers to a collection of data points aggregated together because of certain similarities.

This machine learning project looks at implementing the KMeans clustering algorithm on the wine quality dataset. 
The elbow method is used to find the optimum number of clusters. 
Principle component analysis  (PCA) is used to reduce the dimensionality of the data
The dataset used for this project is available on kaggle and on UCI ML repository. 

 
