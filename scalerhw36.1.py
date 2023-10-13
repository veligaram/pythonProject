class Matrix:
    def __init__(self,r,c):
        self.row=r
        self.column=c
        self.mat=[[0 for j in range(c)] for i in range(r)]
    def input(self):
        for i in range(self.row):
            self.mat[i]=list(map(int,input().split(' ')[:self.column]))
    def add(self, x:"Matrix") -> "Matrix":
        res=Matrix(self.row,self.column)
        for i in range(self.row):
            for j in range(self.column):
                res.mat[i][j]=self.mat[i][j]+x.mat[i][j]
        return res
    def subtract(self,x:"Matrix") -> "Matrix":
        res=Matrix(self.row,self.column)
        for i in range(self.row):
            for j in range(self.column):
                res.mat[i][j]=self.mat[i][j] - x.mat[i][j]
        return res
    def transpose(self) -> "Matrix":
        res=Matrix(self.column,self.row)
        for i in range(self.row):
            for j in range(self.column):
                res.mat[j][i]=self.mat[i][j]
        return res
    def print(self):
        for i in range(self.row):
            for j in range(self.column):
                print(self.mat[i][j],end=" ")
            print()

