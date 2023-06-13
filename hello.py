L = [15,6,7,89,54,76,8,98,32]

def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
    return A

print(L)
bubble_sort(L)
print(L)