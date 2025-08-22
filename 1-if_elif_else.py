# if - é um operador condicional que só será executado caso seja verdadeiro
# a linha deve terminar com ":"
# O bloco do operador deve estar na linha de baixo e com espaçamento

print("Caso if")
continuar = input("Digite 1 para continuar: ")

if continuar == "1":
    print("Programa continuado")

# else - é um operador condicional que representa o caso não ser verdadeiro
# sempre deve ter um if antes
# é sempre o último operador condicional do bloco
# não necessita colocar sua condição

print("Caso if else")
continuar2 = input("Digite 2 para continuar: ")

if continuar2 == "2":
    print("Programa continuado")
else:
    print("Programa interrompido")

# elif - é um operador para acrescntar outras condições entre if e else
# é necessário ter um if antes
#sempre estão entre o if e o else
# Obs: apenas um dos bocos será executado

continuar3 = input("Digite 3 para continuar e 0 para interromper: ")

if continuar3 == "3":
    print("Programa continuado")
elif continuar3 == "0":
    print("Programa interrompido")
else:
    print("Nenhuma das opções foram inseridas")