import random

l4 = ['cicatriz', 'cobertor', 'helicoptero', 'aniversario', 'vulcao', 'arco-iris', 'presidente', 'noiva', 'babar',
      'montanha-russa', 'natal', 'luz', 'sombra', 'magia', 'maquiadora', 'shopping', 'berço', 'medir', 'espelho',
      'aranha', 'moto', 'jardim', 'trampolim', 'cachoeira', 'io-io', 'janela', 'girafa', 'roncar', 'pesadelo',
      'lanterna', 'curiosidade', 'panquecas', 'aplicativo', 'convite', 'adolescente', 'satelite', 'jornal', 'diamante',
      'lenha', 'sapo', 'andador', 'infantil', 'racao', 'google', 'tocha', 'acampar', 'lago', 'emagrecer', 'fofoca',
      'salario', 'sorte']

secreto = l4[random.randint(0, 50)]
digitadas = []
chances = 15

print("Favor digitar em letra minusculas e sem acentos")
while True:
    if chances == 0:
        print('Você Perdeu!!!')
        break

    letra = input("Digite a letra: ")
    if len(letra) > 1:
        print('Vale apenas uma letra')
        continue
    digitadas.append(letra)
    print(digitadas)
    if letra in secreto:
        print(f'UHUUUULL a letra "{letra}" existe na palavra secreta')
    else:
        print(f'AFFFZZ a letra "{letra}" não existe na palavra secreta')
        digitadas.pop()

    secreto_temporario = ""
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f"Legal, você Ganhou!!! a palavra era: '{secreto}.'")
        break
    else:
        print(f'A palavra secreta está assim {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    print(f'Voce ainda tem {chances} Chances\n')