i = 0
li = list()
for i in range(5):
    n = int(input('Digite um numero:'))
    i += 1
    li.append(n)
print(min(li))
li.sort()
print(li)
if 5 in li:
    li.remove(5)
    print('O numero 5 foi removido da lista')
else:
    print('O numero 5 não esta na lista')
print(li)
