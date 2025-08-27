def minTimeToVisitAllPoints(points):
    total_time = 0
    for i in range(1, len(points)):
        x1, y1 = points[i-1]
        x2, y2 = points[i]
        total_time += max(abs(x2 - x1), abs(y2 - y1))
    return total_time
points1 = [[1,1],[3,4],[-1,0]]
print(minTimeToVisitAllPoints(points1))  
points2 = [[3,2],[-2,2]]
print(minTimeToVisitAllPoints(points2))  