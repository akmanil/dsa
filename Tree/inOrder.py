class treeNode():
    def __init__(self ,data):
        self.data = data;
        self.left =None
        self.right = None

def preOrderTransversal(node):
    if node is None:
        return
    preOrderTransversal(node.left);
    print(node.data , end = ',');
    preOrderTransversal(node.right);



root = treeNode("R");
nodeA = treeNode('A')
nodeB = treeNode('B')
nodeC = treeNode('C')
nodeD = treeNode('D')
nodeE = treeNode('E')
nodeF = treeNode('F')
nodeG = treeNode('G')

root.left =nodeA;
root.right = nodeB;

nodeA.left = nodeC;
nodeA.right = nodeD;

nodeB.left = nodeE;
nodeB.right = nodeF;

nodeF.right = nodeG;

preOrderTransversal(root);