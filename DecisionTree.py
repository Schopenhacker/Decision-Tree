# -*- coding: utf-8 -*-

global data, p, class_values, min_size

data = [[2.771244718,1.784783929,0],
    [1.728571309,1.169761413,0],
    [3.678319846,2.81281357,2],
    [3.961043357,2.61995032,2],
    [2.999208922,2.209014212,0],
    [7.497545867,3.162953546,1],
    [9.00220326,3.339047188,1],
    [7.444542326,0.476683375,1],
    [10.12493903,3.234550982,1],
    [6.642287351,3.319983761,1]]
p = 2 # number of predictors
class_values=set([row[-1] for row in data]) #class labels
min_size = 1 #for a leaf

class Node:
    def __init__(self, datanode = None, split_feature_index = p, split_value = None, subnodes = list()):
        self.datanode = datanode
        self.split_feature_index = split_feature_index
        self.split_value = split_value
        self.subnodes = subnodes
    
    def __str__(self):
        return('split_feature_index = {}\nsplit_value{}'.format(self.split_feature_index, self.split_value))
      
    def splited_datanode(self):        
        dataset = self.datanode
        split_index = self.split_feature_index
        split_value = self.split_value
        if (dataset == None or split_index == p or split_value == None):
            return None
        dataleft = list()
        dataright = list()
        for row in dataset:
            if row[split_index] <= split_value:
                dataleft.append(row)
            else:
                dataright.append(row)

        return (dataleft, dataright)
    
    def gini(self):
        # count all samples at the split point
        n_instances = float(len(self.datanode))
        subsets = self.splited_datanode()
        if subsets is None:
            return 999.999
        # sum weighted Gini index for each sub-group
        gini = 0.0
        for sub in subsets:
            n_sub = float(len(sub))
            # prevent our code from dividing by zero
            if n_sub == 0.0:
                continue

            l = [row[-1] for row in sub]
            g = 0.0
            # score the group based on the score for each class
            for c in class_values:
                g += (float(l.count(c))/n_sub)**2

        # weight the group score by its relative size
            gini += (n_sub/n_instances)*(1.0 - g)
        return gini
    
    def isleaf(self):
        """a node is a leaf when it is pure (all remained records have the same class label)
        or when its size is less then min_size"""
        data = self.datanode
        if len(data) < min_size:
            return True
        y = [row[-1] for row in data]        
        for c in class_values:
            if y.count(c) == len(data):
	            return True
        return False
    

    

         
def split_node(node):
    """select the best split for the node"""
 
#   feature = ['X1','X2','Y']
    rand_feature = [0,1]
    dataset = [row for row in node.datanode]
    score = 999
    split_index = -1
    split_value=None
    
    for i in rand_feature:
        for row in dataset:
            node.split_feature_index=i
            node.split_value = row[i]
            gini = node.gini()
            if gini<score:
                score = gini
                split_index = i
                split_value = row[i]

                
    node.split_feature_index=split_index
    node.split_value = split_value
    left, right = node.splited_datanode()
    
    print('\n#----#######------------#######----#')
    print('Best Split: [X%d <|> %.3f] ; gini %.3f' % (split_index+1 , split_value, score))
    print('    left: [X%d <= %.3f]' % (split_index+1 , split_value))
    print('\n'.join(['        '+str(row) for row in left]))
    print('    right: [X%d > %.3f]' % (split_index+1 , split_value))
    print('\n'.join(['        '+str(row) for row in right]))   
    
    nodeleft = Node(datanode = [row for row in left])
    noderight = Node(datanode = [row for row in right])
    node.subnodes=[nodeleft, noderight]

def split(node):
    split_node(node)
    if not node.subnodes[0].isleaf():
        split(node.subnodes[0])
    if not node.subnodes[1].isleaf():
        split(node.subnodes[1])
    return  
    
def classify(root,test):
    if root.isleaf() : return root.datanode[0][-1]
    if test[root.split_feature_index] <= root.split_value:
        return classify(root.subnodes[0],test)
    return classify(root.subnodes[1],test)

if __name__ == '__main__':
	root = Node(datanode = data)
  split(root) 
	print('')   
	test_set = [[3.678319846,2.81281357], [9.00220326, 3.339047188]]
	for test in test_set:
		print('*****\n{} ==> {}'.format(str(test),classify(root, test)))
