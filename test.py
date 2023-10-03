class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def alltest():
        A = [
            [3,4, 5],
            [29, 32, 5]
            
            ]
        B  = 32
        
        low, high = 0, len(A) - 1
        #print(low, high)
        border = -1
        while low <= high:
            mid = (low + high) // 2
            if A[mid][0] < B:
                border = mid
                low = mid + 1
                
            elif A[mid][0] > B:
                high = mid - 1
            elif A[mid][0] == B:
                return 1
        print(border)        
        def searchrow(row):
            left, right = 0, len(row) - 1
            while left <= right:
                midl = (left + right) // 2
                if row[midl] < B:
                    print(row[midl], 'less than', B)
                    left = midl + 1
                elif row[midl] > B:
                    print(row[midl], 'greater than', B)
                    right = midl - 1
                elif row[midl] == B:
                    print('in this found')
                    return 1
                    print("found")
            return 0

        if border == -1:
            return 0
        else:
            for i in range (0, border + 1):
                
                searchrow(A[i])
        return 0
    op = alltest()
    print('op', op)
            
        
            
                
                
                
                
                