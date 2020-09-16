A = [1,3,7,9,14,16,17,19,19,19,20,21,25,26,26,27,27,27,28,29]
n = len(A)
K = int(input(("Введите число:")))

for i in range(n):
    if A[i] > K < A[i+1]:
       s = i
       break
    elif K >= A[len(A) - 1]:
        s = len(A)
        break
    elif K < A[0]:
        s = 0
        break
print(s)