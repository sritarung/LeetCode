class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
        # given a list of points
        # count no. of pairs of points that meet
            # A point is on upper left side of B
            # no points in the line or rectangle they make
        

         # naive n^3 approach
        ans = 0
        n = len(points)

        for i in range(n):
            A = points[i]
            for j in range(n):
                B = points[j]
                if i == j or not (A[0] <= B[0] and A[1]>= B[1]):
                    continue
                
                if n == 2:
                    ans += 1
                    continue
                illegal = False
                for k in range(n):
                    if k == i or k == j:
                        continue
                    
                    temp = points[k]
                    isX = (temp[0]>= A[0] and temp[0]<= B[0])
                    isY = (temp[1]<=A[1] and temp[1]>=B[1])

                    if isX and isY:
                        illegal = True
                        break
                if not illegal:
                    ans += 1
        return ans


