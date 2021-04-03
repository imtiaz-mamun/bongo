class getNode:
    def __init__(self, data):
        self.key = data
        self.data = data 
        self.left = self.right = None
  
# path
def hasPath(root, arr, x):
    if (not root):
        return False
      
    arr.append(root.data)     
    
    if (root.data == x):     
        return True
    
    if (hasPath(root.left, arr, x) or 
        hasPath(root.right, arr, x)): 
        return True
    arr.pop(-1) 
    return False
  
def printPath(root, x):
    arr = [] 
    if (hasPath(root, arr, x)):
        for i in range(len(arr) - 1):
            print(arr[i], end = "->") 
        print(arr[len(arr) - 1])
      
    else:
        print("No Path")

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
def findLCA(root, n1, n2):
    path1 = []
    path2 = []
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1
 
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]
        
# Main
if __name__ == '__main__':
    root = getNode(1) 
    root.left = getNode(2) 
    root.right = getNode(3) 
    root.left.left = getNode(4) 
    root.left.right = getNode(5) 
    root.right.left = getNode(6) 
    root.right.right = getNode(7) 
    root.left.left.left = getNode(8) 
    root.left.left.right = getNode(9) 
    x = input("Find Ancestors of Node:")
    printPath(root, int(x))
    print("Find LCA of Nodes:")
    print ("LCA: ",findLCA(root,int(input("Node 1:")), int(input("Node 2:"))))
