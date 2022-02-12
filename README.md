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

![index](https://previews.dropbox.com/p/thumb/ABeTnGGQa-_iyNiSApUYULs9L9VnwLb7ZEqWzk__QQLknwl5FAjeEMb4gDZeoRW8J71mEryTMn_EpwwPLBVuUlePpHUj95IpJKfDgENfSdu89_PIPSrD1Ls3IU6d7h4Tlx1WMFJYutWuTaggLI2gIFC7SlTzsuzwayuQUYgJEIlAYD7rhQL0NNdwXpsW-RZo_-dBN26RtmcolcJImL-iVGorlBkR-oy4In8Q87dKRLRMlOoFlI5BADQlw6xkthyMxtXsH6QBIoOHhsGKYeqwIXcgqQ-3JuLMA8qm1yEXtnDjwzksEp7MXs7q72eoXZ5A7L9yvF_2F-8XuQlOBCWcq2BFC6gNPvDhoX1ykKzLPSLGLg/p.png)

**Problem Statement**

In this projecct, The popular Titanic dataset is used(Available on kagel). I try to classify weather or not a passager will survive the the crash./n  To do this, the Decision Tree Classifier was used.
The Python implementation is presented in the Jupyter notebook

**Result**

The Decision tree model accuracy score is  0.83 and 10-fold cross validation average accuracy: 0.79.So, the model does a very good job in predicting whether or not a passenger will survive or not.
