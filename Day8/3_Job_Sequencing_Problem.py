'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        Jobs = sorted(Jobs, key=lambda job: (-job.profit, job.deadline))

        max_deadline = -1
        for i in Jobs:
           max_deadline = max(max_deadline, i.deadline)
           
        days = [-1] * max_deadline
            
        time = 1
        no_of_job = 0
        profit = 0


        for i in range(n):
            for j in range(Jobs[i].deadline-1, -1, -1):
                if days[j] != -1:
                    continue
                days[j] = Jobs[i].id
                no_of_job += 1
                profit += Jobs[i].profit
                break
        
        return [no_of_job, profit]
