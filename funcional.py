import math
from typing import Callable


def soma(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


# salvando uma função em uma variável
somar: Callable[[int,int], int] = soma
print(somar(2, 3))


# passando uma função como parâmetro
def operacao_aritimetica(fn: Callable[[int, int], int], op1: int, op2: int):
    return fn(op1, op2)

print(operacao_aritimetica(soma, 13, 48))
print(operacao_aritimetica(sub, 13, 48))


# usando lambdas
lambda_teste: Callable[[int, int], float] = lambda a, b: math.pow(a, b)
print(lambda_teste(5, 2))


# processamento de uma função em duas etapas: bom para usar em casos que demandem de muito processamento
def soma_parcial(a: int) -> Callable[[int], int]:
    def concluir_soma(b: int) -> int:
        return a + b
    return concluir_soma

primeira_soma = soma_parcial(500)
print(primeira_soma(500))
print(primeira_soma(1000))
print(primeira_soma(1))
