# Decision-Tree

When i was searching tutorials about decision tree implementation i noticed that all of them use sklearn library for that, so i thought it would be pretty nice to try to implement it by my own without recourse to any predefined script
To do that, we had to deeply understand the algorithm of Decision Tree

So in this projet, i will try to implement the Classification Decision Tree algorithm with Python.
to do so, we need the know how to address the following issues:

* Evaluate candidate split points in a data:
  * which attribute we ought to choose to partition the data making the data as purer as possible?
  * when a node is considered a leaf (terminal node corresponding to a class label) ?
* Arrange splits into a decision tree structure.
* Alassify a test set : each record is made up of only predictors and we have to find out its class label
