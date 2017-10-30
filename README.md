# Decision-Tree Implementation

When i was searching tutorials about decision tree implementation i noticed that all of them use sklearn library for that, so i thought it would be pretty nice to try to implement it by my own without recourse to any predefined script.
to be able to implement each step , we have no choice but to dive into DecisionTree algorithm to get through all of its nuts and bolts.

So in this projet, i will try to implement the Classification Decision Tree algorithm with Python.
To do so, we need the know how to address the following issues:

* Evaluate candidate split points in a data:
  * which attribute we ought to choose to partition the data making the data as purer as possible?
  * when a node is considered a leaf (terminal node corresponding to a class label) ?
* Arrange splits into a decision tree structure.
* Classify a test set : each record is made up of only predictors and we have to find out its class label

## Classification
In this project we will discuss the classification Decision Tree Algorithm
First of all, let me explain what is a Classifcation model and how an algorithm process in general to classify data
input : a structured dataset with a set of attributes
![relational table lookslike](https://upload.wikimedia.org/wikipedia/en/b/b7/Relational_db_terms.png)
we can identify an implicit hidden pattern:
 each record = tuple(X,Y)
 * X : attribute set or predictors
 * Y : a special attribute

General Approach :
* Training Set : 
We dipose of a dataset with known class labels for each record
We feed the algo with such training data so that it learns the general rules that describe the relationship between x and y: and builds a classification model that maps each x to y
* Test set :
for each record we only dispose of the values of X
we figure out the class label y given the values of the predictors X by appling the classification model built with the training set

Such process is called supervised learning, because we "help" the algorithm by providing a preclassified dataset.

## Decision Tree Classification
We can summarize crafted questions, which can approximate the class label, with a decision Tree.
### Decision Tree Terminologie:
* Each leaf node (terminal node) corresponds to a class label
* Each non-terminal node (root or internal node) contains an attribute test condition
![DT Classifier example](http://mines.humanoriented.com/classes/2010/fall/csci568/portfolio_exports/lguo/image/decisionTree/decisionTree.jpg)
![DT Classifier] (http://mines.humanoriented.com/classes/2010/fall/csci568/portfolio_exports/lguo/image/decisionTree/decisionTree.jpg)
