a = int(input())
b = int(input())
for i in range(a,b + 1):
   d = len(str(i))
   sum = 0
   c = i
   while c > 0:
       e = c % 10
       sum += e ** d
       c //= 10
   if i == sum:
       print(i)
