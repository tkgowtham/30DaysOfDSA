class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        
        # code here
        acts = [(end[i], start[i]) for i in range(n)]
        acts.sort()
        ans = 1
        
        limit = acts[0][0]
        for i in range(n):
            if acts[i][1] > limit:
                ans += 1
                limit = acts[i][0]
              
        return ans
