# Find max 10 numbers in a list having 10M entries.
def largest(arr , n, k):
    import heapq
    final = []
    temp = []
    for i in range(n):
        heapq.heappush(temp,-arr[i])
    for i in range(k):
        final.append(temp[0])
        temp.pop()
    return final