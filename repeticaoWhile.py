# -*- coding: utf-8 -*-
num = int(input("Insira um número: "))

while num != 0:
    soma = soma + (num % 10)
    num = num // 10

print(soma)