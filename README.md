# Decision-Tree

When i was searching tutorials about decision tree implementation i noticed that all of them use sklearn library for that, so i thought it would be pretty nice to try to implement it by my own without recourse to any predefined script.
to be able to implement each step , we have no choice but to dive into DecisionTree algorithm to get through all of its nuts and bolts.

So in this projet, i will try to implement the Classification Decision Tree algorithm with Python.
To do so, we need the know how to address the following issues:

* Evaluate candidate split points in a data:
  * which attribute we ought to choose to partition the data making the data as purer as possible?
  * when a node is considered a leaf (terminal node corresponding to a class label) ?
* Arrange splits into a decision tree structure.
* Classify a test set : each record is made up of only predictors and we have to find out its class label
