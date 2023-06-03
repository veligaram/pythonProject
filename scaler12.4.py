#to print the square of then numbers
def square_of_numbers():
    n=int(input())
    answer=(n*(n+1)*(2*n+1))//6 #formula
    return answer
print(square_of_numbers())