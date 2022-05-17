#Rotate by 90 degree ----------------------------------------------------------------

def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(0,rows):
        for j in range(i+1,rows):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(0,rows):
        low = 0
        high = rows-1
        while low < high:
            matrix[low][i], matrix[high][i] = matrix[high][i], matrix[low][i]
            low += 1
            high -= 1