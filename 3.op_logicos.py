# # Operadores lógicos 
# # and (e) or (ou) not (não) None
# # None - representa um não valor

# # and - todas as condições necessitam ser verdadeiras
# # Se uma condição for False, ela será considerada esse valor
# # Será interrompido no momento que for encontrada uma False
# # Expressões False: 0 0.0 '' False

# entrada = input("[E]ntrar [S]air: ")
# senha_input = input("Digite sua senha: ")

# senha = "123"

# if entrada == "E" and senha_input == senha:
#     print("Entrada permitida")
# else:
#     print("Entrada não permitida")

# # # Avaliação de curto circuito - irá avaliar onde a ação é interrompida

# print(True and False and True)
# print(True and 0 and True)

# # or - retorna a primeira condição como verdadeira

# entrada = input("[E]ntrar [S]air: ")
# senha_input = input("Digite sua senha: ")

# senha = "123"

# if (entrada == "E" or entrada == "e") and senha_input == senha:
#     print("Entrada permitida")
# else:
#     print("Entrada não permitida")

# # Avaliação de curto circuito - irá avaliar onde a ação é interrompida

# print("123" or False or False)
# print(False or False or "456")

# # not - Utilizado para inverter a expressãp

# print(not False)
# print(not True)
# print(not 0)
# print(not 1)

# in - Utilizado para procurar informações 

name_ex = "Guimarães"
print("Gui" in name_ex)
print("gui" in name_ex)
print("G" not in name_ex)
print("A" not in name_ex)

name = input("Digite seu nome: ")

find = input("Digite o que deseja encontrar: ")

if (find in name):
    print(find)
else:
    print("Não encontrado")
