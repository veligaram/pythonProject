# Take input an array A of size N and write a program to print maximum and minimum elements of the input.
# The only line of input would contain a single integer N that represents the length of the array followed by the N elements of the input array A.
def max_min(N,lst):
    maximum_element=max(lst)
    minimum_element=min(lst)
    return maximum_element,minimum_element
print(max_min(5,[4,7,2,7,9]))
