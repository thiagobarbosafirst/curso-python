# -*- coding: utf-8 -*-
num = input("Digite um número inteiro: ")
numInt = int(num)

if (numInt % 3) == 0 and (numInt % 5) == 0: 
    print("FizzBuzz")
else:
    print(num)
