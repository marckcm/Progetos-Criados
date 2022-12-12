lista = """


cole os links aqui
o separador esta configurado para separar sempre que tiver uma virgula e um espaço so alterar se o texto estiver
separado com barras por ex:

casa/predio/edificio/rua/carro/troque ', ' po '/' ou algo no texto que se repita tipo um espaço " "


texto


"""

sites = lista.split(', ')
print(sites)
for item in sites:
    print(item)

