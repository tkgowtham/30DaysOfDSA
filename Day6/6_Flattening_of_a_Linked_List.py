#O(2*N*M) O(1)

def merge(list1, list2):
    dummy = Node(-1)
    res = dummy
    
    while list1 != None and list2 != None:
        if list1.data < list2.data:
            res.bottom = list1
            res = list1
            list1 = list1.bottom
        else:
            res.bottom = list2
            res = list2
            list2 = list2.bottom
            
        res.next = None
        
    if list1 != None:
        res.bottom = list1
    
    if list2 != None:
        res.bottom = list2
        
    if dummy.bottom != None:
        dummy.bottom.next = None
        
    return dummy.bottom
    

def flatten(root):
    #Your code here
    if root == None or root.next == None:
        return root
        
    mergedHead = flatten(root.next)
    root = merge(root, mergedHead)
    return root
