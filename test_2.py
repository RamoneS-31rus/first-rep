print("Введите числа через пробел. По окончании ввода нажмите Enter")
a = input().split()

n = len(a)

print(a)
print(n)

def sort(a_sort):
    for num in range(len(a_sort)-1,0,-1):
        for i in range(num):
            if a_sort[i]>a_sort[i+1]:
                temp = a_sort[i]
                a_sort[i] = a_sort[i+1]
                a_sort[i+1] = temp

a_sort = a
sort(a_sort)
print(a_sort)