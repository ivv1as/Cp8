a =''
b=''
print('Введите число')
try:
	c=int(input())
except ValueError:
	print('Введенные данные не являются целым числом')
	exit()
else:
	print('Введите систему счисления')
try:
	d=int(input())
except ValueError:
	print('Введенные данные не являются целым числом')
	exit()
else:
	if d==2:
		while c>0:
			a=str(c%2)+a
			c=c//2
print(a)
if d==8:
	while c>0:
		b=str(c%8)+b
		c=c//8
print(b)