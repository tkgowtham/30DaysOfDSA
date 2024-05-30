#TC = O(N) + O(NlogN) SC = O(N)
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        meets = [(end[i], start[i]) for i in range(n)]
        meets.sort()
        ans = 1
    
        
        limit = meets[0][0] #end time of first meeting
        for i in range(1,n):
            if meets[i][1] > limit:
                ans += 1
                limit = meets[i][0]
        
        return ans
