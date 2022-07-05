#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9
"""

__version__ = "0.1.0"

import sys
import operator

ops = {
    "sum": operator.add,
    "mul": operator.mul,
    "sub": operator.sub,
    "div": operator.truediv,
}

arguments = sys.argv[1:]
op = None
number = []
values = []
if not arguments:
	op = input("Qual a operação desejada (sum, sub, mult e div): ")
	if op not in ops:
		print(f"Operação inválida: {op}")
		exit(1)
	number.append(input("v1: "))
	number.append(input("v2: "))
elif len(arguments) != 3:
	print("A operação de seguir o formato:")
	print("[operador] [valor1] [valor2]")
	print("Operadores aceitos: sum, sub, mul e div")
	exit(1)
elif not number:
	op = arguments[0]
	number = arguments[1:]
for val in number:
	if val.isdigit():
		values.append(int(val))
	elif val.replace(".", "").isdigit():
		values.append(float(val))
	else:
		print("Os valores devem ser números inteiros ou decimais!")
		exit(1)
op = ops[op]
print(op(values[0], values[1]))