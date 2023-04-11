import os

caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo: ')
conta = 0


def formata_tamanho(tamanho):
    base = tamanho
    kilo = 1000
    mega = kilo ** 2
    giga = kilo ** 3
    tera = kilo ** 4
    peta = kilo ** 5

    if tamanho < kilo:
        tamanho = base
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 2)
    return f'{tamanho} {texto}'.replace('.', ',')


for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                print()
                print('Encontri o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extenção: ', ext_arquivo)
                print('Tamanho: ', tamanho)
                print('Tamanho formatado: ', formata_tamanho(tamanho))

            except PermissionError as e:
                print('Sem permissões.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido:', e)

print()
print(f'{conta} arquivo(s) encontrado')




