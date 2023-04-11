# Importando CSV
import csv

lista = ['mais1', 'MASCULINO', '1200345116', 'marckcm@gmail.com']


# Função add
def adicionar_dados(i):
    with open('dados.csv', 'a+', newline='') as file:
        escrever = csv.writer(file)
        escrever.writerow(i)


# Função ver dados:
def ver_dados():
    dados = []
    # Acessando csv
    with open('dados.csv') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            dados.append(linha)
    return dados


# Função remover dados:
def remover_dados(i):

    def adicionar_novalista(j):
        with open('dados.csv', 'w', newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)
            ver_dados()

    nova_lista = []
    telefone = i
    with open('dados.csv', 'r') as file:
        ler_csv = csv.reader(file)

        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == telefone:
                    nova_lista.remove(linha)

    # Adicionando nova lista
    adicionar_novalista(nova_lista)


# Função atualizar dados:
def atualizar_dados(i):
    def adicionar_novalista(j):
        with open('dados.csv', 'w', newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)
            ver_dados()

    nova_lista = []
    telefone = i[0]
    with open('dados.csv', 'r') as file:
        ler_csv = csv.reader(file)

        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == telefone:
                    nome = i[1]
                    sexo = i[2]
                    tel = i[3]
                    email = i[4]

                    dados = [nome, sexo, tel, email]

                    # Trocando a lista
                    index = nova_lista.index(linha)
                    nova_lista[index] = dados

    # Adicionando nova lista
    adicionar_novalista(nova_lista)


# Função pesquisar dados:
def pesquisar_dados(i):
    dados = []
    telefone = i
    with open('dados.csv') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            for campo in linha:
                if campo == telefone:
                    dados.append(linha)
    return dados





