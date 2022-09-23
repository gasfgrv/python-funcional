from functools import reduce

# usando o map()
notas = [6.4, 7.2, 5.8, 8.4]

def acrescenta_nota(delta):
    def calcular(nota):
        return nota + delta
    return calcular

notas_finais = list(map(acrescenta_nota(1.5), notas))
print(list(notas_finais))


# usando map() com lambda e list comprehension
notas_finais_lambda = [*map(lambda nota: nota + 1.5, notas)]
print(notas_finais_lambda)


# reduce
def somar(a, b):
    return a + b

total = reduce(somar, notas, 0)
print(total)


# reduce usando lambda
total_lambda = reduce(lambda total, nota: total + nota, notas, 0)
print(int(total_lambda))
