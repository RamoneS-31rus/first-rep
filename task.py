A = [1, 3, 7, 9, 14, 16, 17, 19, 19, 19, 20, 21, 25, 26, 26, 27, 27, 27, 28, 29]
K = int(input()) #вводим число и преобразуем его в целое
n = len(A) #присваиваем переменной длину массива
mid = n//2 #находим индекс середины массива
low = 0 #минимальный индекс массива
high = n - 1 #максимальный индекс массива
s = 0 #присваиваем переменной вывода начальное значение
print(A) #вывод всего массива
while low <= high: #пока минимальный индекс меньше или равен максимальному индексу
   if K<A[0]: #если введенное число меньше первого числа массива
       s = 0 #то переменная вывода равна нулю
       break #выход из цикла
   elif K>A[len(A) - 1]: #если введенное число больше последнего числа массива
       s = len(A) #то переменная вывода равна длине массива (получается что индекс будет на 1 больше, чем у последнего числа массива)
       break #выход из цикла
   elif A[mid] < K < A[mid + 1]: #если введенное число больше числа середины массива, но меньше следующего числа массива
       s = mid + 1 #то индекс переменной вывода на 1 больше индекса середины массива
       break #выход из цикла
   elif A[mid] == K: #если введенное число равно числу середины массива
       if mid != len(A) - 1: #и если индекс середины массива не равен последнему индексу массиву
           i = mid + 1 #вводим переменную i со значением индекса середины массива плюс 1
           while A[i] == K: #пока значение переменной i равно введенному числу
               i+=1 #увеличиваем значение i на 1
           s = i #по завершению цикла присваиваем переменной вывода значение переменной i
           break #выход из цикла
       else: #иначе
           s = len(A) #значение переменной вывода равно длине массива
           break #выход из цикла
   elif K > A[mid]: #если введенное число больше числа середины массива
       low = mid + 1 #то минимальный индекс равен индексу середины массива плюс 1
   else: #иначе
       high = mid - 1 #максимальный индекс равен индексу середины массива минус 1
   mid = (low + high) // 2 #находим индекс середины нового интервала(Половиним левую или правую часть сначало изначального массива, потом предыдущего интервала. Продолжаем дробить массив на части пока не найдем искомое значение)
print(s) #выводим индекс введеного числа