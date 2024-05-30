class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        
        # code here

        arr = sorted(arr, key=lambda a: (-a.value/a.weight))
        
        curr_w = 0
        curr_v = 0

        for i in range(n):
            if curr_w + arr[i].weight <= w:
                curr_w += arr[i].weight
                curr_v += arr[i].value
            else:
                remain = w - curr_w
                curr_v += (arr[i].value/arr[i].weight) * remain
                break
        
        return curr_v
