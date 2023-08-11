def transpose(matrix):
    transpose=[]
    for i in range(len(matrix[0])):
        transpose.append([row[i] for row in matrix])
    return transpose
print(transpose([[1,2,3,4],[5,6,7,8]]))