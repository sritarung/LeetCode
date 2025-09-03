class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
        # given a list of points
        # count no. of pairs of points that meet
            # A point is on upper left side of B
            # no points in the line or rectangle they make
        

        # n^2 approach with sorting
        points.sort(key = lambda x: (x[0], -x[1]))
        pair_count = 0
        n = len(points)

        for i in range(n):
            upper_y = points[i][1]
            lower_y = float('-inf')
            for j in range(i+1, n):
                curr_y = points[j][1]
                if curr_y <= upper_y and curr_y > lower_y:
                    pair_count += 1
                    lower_y = curr_y
                    if curr_y == upper_y:
                        break
        return pair_count

