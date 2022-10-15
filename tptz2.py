print("Введите название файла")
fileName = input()
file = open(fileName)
x = file.readline()
x = x.split()
for i in range(len(x)):
    x[i] = int(x[i])
def _min(x):
   min = x[0]
   for i in x:
       if i < min:
          min = i
   return min
print(_min(x))
def _max(x):
   max = x[0]
   for i in x:
       if i > max:
          max = i
   return max
print(_max(x))
def _sum(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum
print(_sum(x))
def mult(x):
    mult = 1
    for i in range(len(x)):
        mult = mult * x[i]
    return mult
print(mult(x))

