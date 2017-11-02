from node import Node

DATA = [[2.771244718,1.784783929,0],
    [1.728571309,1.169761413,0],
    [3.678319846,2.81281357,2],
    [3.961043357,2.61995032,2],
    [2.999208922,2.209014212,0],
    [7.497545867,3.162953546,1],
    [9.00220326,3.339047188,1],
    [7.444542326,0.476683375,1],
    [10.12493903,3.234550982,1],
    [6.642287351,3.319983761,1]]

def split_node(node):
    """select the best split for the node"""
 
#   feature = ['X1','X2','Y']
    rand_feature = [0,1]
    dataset = [row for row in node.datanode]
    score = 999
    split_index = -1
    split_value = None
    
    for i in rand_feature:
        for row in dataset:
            node.split_feature_index = i
            node.split_value = row[i]
            gini = node.gini()
            if gini < score:
                score = gini
                split_index = i
                split_value = row[i]
    
    node.split_feature_index = split_index
    node.split_value = split_value
    left, right = node.splited_datanode()
    
    print('\n#----#######------------#######----#')
    print('Best Split: [X%d <|> %.3f] ; gini %.3f' % (split_index + 1, split_value, score))
    print('\tleft: [X%d <= %.3f]' % (split_index + 1, split_value))
    print('\n'.join(['\t\t' + str(row) for row in left]))
    print('\tright: [X%d > %.3f]' % (split_index + 1, split_value))
    print('\n'.join(['\t\t' + str(row) for row in right]))
    
    node_left = Node(datanode=[row for row in left])
    node_right = Node(datanode=[row for row in right])
    node.subnodes = [node_left, node_right]

def split(node):
    split_node(node)
    if not node.subnodes[0].is_leaf():
        split(node.subnodes[0])
    if not node.subnodes[1].is_leaf():
        split(node.subnodes[1])
    
def classify(root, test):
    if root.is_leaf(): return root.datanode[0][-1]
    if test[root.split_feature_index] <= root.split_value:
        return classify(root.subnodes[0], test)
    
    return classify(root.subnodes[1], test)

if __name__ == '__main__':
    root = Node(datanode=DATA)
    split(root)
    print('')
    test_set = [[3.678319846,2.81281357], [9.00220326, 3.339047188]]
    for test in test_set:
        print('*****\n{} ==> {}'.format(str(test), classify(root, test)))

		
		
		
