#TC = O(N) + O(NlogN) SC = O(1)

def minimumPlatform(self,n,arr,dep):
        # code here
        #times = [(arr[i], dep[i]) for i in range(n)]
        #times.sort()
        #arr = [times[i][0] for i in range(n)]
        #dep = [times[i][1] for i in range(n)]
        
        arr.sort()
        dep.sort()
        
        platforms_needed = max_platforms = 1
    
        i = 1
        j = 0
        
        while i < n and j < n:
            if arr[i] <= dep[j]: #A train arriving before a train is going to depart
                platforms_needed += 1
                i += 1
            elif arr[i] > dep[j]: #Train arrving after a train departs.
                platforms_needed -= 1
                j += 1
                
            if platforms_needed > max_platforms:
                max_platforms = platforms_needed
        
        return max_platforms
