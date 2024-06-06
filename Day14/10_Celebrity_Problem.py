def findCelebrity(n, matrix):
    for i in range(n):
        is_celebrity = True
        for j in range(n):
            if i != j and (matrix[i][j] == 1 or matrix[j][i] != 1):
                is_celebrity = False
                break
              
        if is_celebrity:
            return i
    return -1 
