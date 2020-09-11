A = [1, 3, 7, 9, 14, 16, 17, 19, 19, 19, 20, 21, 25, 26, 26, 27, 27, 27, 28, 29]
K = int(input())
n = len(A)
mid = n//2
low = 0
high = n-1
s = 0
print(A)
while low <= high:
   if K<A[0]:
       s=0
       break
   elif K>A[len(A)-1]:
       s = len(A)
       break
   elif A[mid] < K < A[mid + 1]:
       s = mid+1
       break
   elif A[mid] == K:
       if mid != len(A) - 1:
           i = mid+1
           while A[i] == K:
               i+=1
           s = i
           break
       else:
           s = len(A)
           break
   elif K > A[mid]:
       low = mid + 1
   else:
       high = mid - 1
   mid = (low + high) // 2
print(s)
