
print("Texto explicativo sobre o exercício e suas respostas\n")

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
        },
        'resposta_certa': 'd'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 2x2? ',
        'respostas': {
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
        },
        'resposta_certa': 'd'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 2/2? ',
        'respostas': {
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
        },
        'resposta_certa': 'a'
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 2-2? ',
        'respostas': {
            'a': '0',
            'b': '2',
            'c': '3',
            'd': '4',
        },
        'resposta_certa': 'a'
    },
}

respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv["resposta_certa"]:
        print('Você acertou')
        respostas_certas += 1
    else:
        print('Você errou')

qnt_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qnt_perguntas * 100

print(f'\nVocê acertou {respostas_certas} respostas')
print(f'Sua porcentagem de acertos foi de {porcentagem_acerto}%.')
