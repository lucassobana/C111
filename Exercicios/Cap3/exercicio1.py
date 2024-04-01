# Lucas Sawada Obana - 241 - GES

# Exercicio 1
print("Exercicio 1")

seleções = ["Arsenal", "Manchester United", "Manchester City", "Liverpool", "Real Madrid"]

# Alternativa A
print("3 primeiros colocados: ", seleções[:3])

# Alternativa B
print("2 ultimos colocados: ", seleções[3:])

# Alternativa C
seleções.sort()
print("Selecoes em ordem alfabetica: ", seleções)

# Alternativa D
print("Liverpool esta na posicao: ", seleções.index("Liverpool"))

print("--------------------------------------------")

# Exercicio 2
print("Exercicio 2")

loja_1 = {"iphone 15", "iphone 13", "Samsung Galaxy S23", "Samsung Galaxy S22","Xiaomi Mi 11"}
loja_2 = {"iphone 13", "iphone 12", "Samsung Galaxy S22", "Redmi note 10", "Redmi note 11"}

print("Modelos disponiveis na loja 1 ", loja_1)
print("Modelos disponiveis na loja 2 ", loja_2)

# ENCONTR O TOTAL DE MODELOS DISPONIVEIS
total = loja_1 | loja_2
print("Total de modelos disponiveis: ", total)

# Encontre os modelos que estão disponíveis em ambas as lojas
modelos_comum = loja_1 & loja_2
print("Modelos disponiveis em ambas as lojas:", modelos_comum)

print("--------------------------------------------")

# Exercicio 3
print("Exercicio 3")

def situacao(media):
    if media >= 60:
        return "AP"
    else:
        return "RP"

alunos = {}

num_alunos = int(input("Quantos alunos deseja cadastrar? "))

for i in range(num_alunos):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    media = float(input(f"Digite a media do {i+1}º aluno: "))

    situacao = situacao(media)

    alunos[nome] = {"media": media, "situacao": situacao}

print("\nConteudo do dicionario:")
for nome, info in alunos.items():
    print(f"Nome: {nome} - Media: {info['media']} - Situacao: {info['situacao']}")
