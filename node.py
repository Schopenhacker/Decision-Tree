PREDICTOR_COUNT = 2 # number of predictors
MIN_SIZE = 1 #for a leaf

class Node:
    def __init__(self, datanode=None, split_feature_index=PREDICTOR_COUNT, split_value=None, subnodes=list()):
        self.datanode = datanode
        self.class_values = set([row[-1] for row in self.datanode]) #class labels
        self.split_feature_index = split_feature_index
        self.split_value = split_value
        self.subnodes = subnodes
    
    def __str__(self):
        return 'split_feature_index = {}\nsplit_value{}'.format(self.split_feature_index, self.split_value)
      
    def splited_datanode(self):        
        if (self.datanode == None or self.split_feature_index == PREDICTOR_COUNT or self.split_value == None):
            return None
        
        data_left = list()
        data_right = list()
        for row in self.datanode:
            if row[self.split_feature_index] <= self.split_value:
                data_left.append(row)
            else:
                data_right.append(row)

        return (data_left, data_right)
    
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
            for c in self.class_values:
                g += (float(l.count(c))/n_sub)**2

            # weight the group score by its relative size
            gini += (n_sub/n_instances) * (1.0-g)
        
        return gini
    
    def is_leaf(self):
        """a node is a leaf when it is pure (all remained records have the same class label)
        or when its size is less then MIN_SIZE"""
        if len(self.datanode) < MIN_SIZE:
            return True
        
        y = [row[-1] for row in self.datanode]
        for c in self.class_values:
            if y.count(c) == len(self.datanode):
                return True
        
        return False