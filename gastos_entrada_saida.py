cadastro_entrada = []
cadastro_saida = []
soma_entrada = 0
soma_saida = 0

while True:
    tipo = int(input('[1] Valores de Entrada\n'
                     '[2] Valores de Saída\n'
                     '[3] Imprimir Tabela\n'
                     'Escolha: '))
    if tipo == 1:
        while True:
            dado = float(input('Insira o valor: '))
            cadastro_entrada.append(dado)
            confirmar = str(input('Adicionar mais valores de ENTRADA?'
                                  '\n(S/N): ')).upper().strip()
            if confirmar == 'S':
                continue
            else:
                tipo = None
                break
    elif tipo == 2:
        while True:
            dado = float(input('Insira o valor: ')) * (-1)
            cadastro_saida.append(dado)
            confirmar = str(input('Adicionar mais valores de SAÍDA?'
                                  '\n(S/N): ')).upper().strip()
            if confirmar == 'S':
                continue
            else:
                tipo = None
                break
    elif tipo == 3:
        break

itab = 0

if len(cadastro_entrada) > len(cadastro_saida):
    itab = len(cadastro_entrada) - len(cadastro_saida)
    for i in range(itab):
        cadastro_saida.append(0)
elif len(cadastro_entrada) < len(cadastro_saida):
    itab = len(cadastro_saida) - len(cadastro_entrada)
    for i in range(itab):
        cadastro_entrada.append(0)

print('\U0001f539'*20,
      '\n|  Entrada  |-|   Saída   |')
for i in range(0, len(cadastro_entrada) and len(cadastro_saida)):
    soma_entrada += cadastro_entrada[i]
    soma_saida += cadastro_saida[i]
    print(f'|{cadastro_entrada[i]:11.2f}|-|{cadastro_saida[i]:11.2f}|')
print('\U0001f059'*18)

total = soma_entrada + soma_saida

print(f'|{soma_entrada:11.2f}|-|{soma_saida:11.2f}|',
      '\n', '\U0001f059'*17,
      f'\n|Total:{total:19.2f}|'
      '\n', '\U0001f539'*18)
