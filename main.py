'''Crie um programa de aplicativo de cinema que faça o seguinte:
- O usuário informa nome e idade.
- O programa mostra uma lista de 5 filmes, a sala em que cada filme está passando, e a classificação indicativa (idade mínima) de cada filme.
- O usuário informa a sala onde está passando o filme desejado.
- Se o usuário tiver a idade mínima para o filme, o programa imprime o ingresso e encerra a aplicação.
- Se o usuário não tiver a idade mínima para o filme, o programa proíbe a entrada e solicita ao usuário que decida por outro filme.

Ao terminar, faça o commit e envie para um repositório remoto no GitHub, e por fim responda a atividade colando o link do repositório.'''

import os
# recebendo nome do usuario
nome = input('Informe seu nome: ')
idade = str(input(f'Informe sua idade: '))
idade = float(idade)

# exibe lista de filmes e suas salas
print('Lista de filmes \n')
print('Sala 1: A volta dos que não foram. \n Classificação indicativa: 10 anos')
print('Sala 2: A roda quadrada. \n Classificação indicativa: 8 anos')
print('Sala 3: Poeira em alto mar.\n Classificação indicativa: 12 anos')
print('Sala 4: As tranças do rei careca.\n  Classificação indicativa: 16 anos')
print('Sala 5: a vingança do peixe frito.\n Classificação indicativa: 16 anos \n')

if idade <= 9:
    print(f'{nome}, desculpe mas você não tem idade para assistir a nenhum dos filmes...')
else:
# recebendo a sala escolhida
    while True:
        sala = int(input('Infrome qual a sala desejada: '))
        match sala:
            case 1:
                if idade <=9:
                    print(f'{nome}! você não possui idade o suficiente para assistir a esse filme. Por favor escolha novamente uma sala')
                    continue
                elif idade >= 10:
                    print(f'{nome}! O filme escolhido por você foi: A volta dos que não foram')
                    break
            case 2:
                if idade <= 8:
                    print(
                        f'{nome}! você não possui idade o suficiente para assistir a esse filme. Por favor escolha novamente uma sala')
                    continue
                elif idade >= 8:
                    print(f'{nome}! O filme escolhido por você foi: A roda quadrada')
                    break
            case 3:
                if idade <= 12:
                    print(
                        f'{nome}! você não possui idade o suficiente para assistir a esse filme. Por favor escolha novamente uma sala')
                    continue
                elif idade >= 12:
                    print(f'{nome}! O filme escolhido por você foi: Poeira em alto mar')
                    break
            case 4:
                if idade <= 16:
                    print(
                        f'{nome}! você não possui idade o suficiente para assistir a esse filme. Por favor escolha novamente uma sala')
                    continue
                elif idade >= 16:
                    print(f'{nome}! O filme escolhido por você foi: As tranças do rei careca')
                    break
            case 5:
                if idade <= 16:
                    print(
                        f'{nome}! você não possui idade o suficiente para assistir a esse filme. Por favor escolha novamente uma sala')
                    continue
                elif idade >= 16:
                    print(f'{nome}! O filme escolhido por você foi: a vingança do peixe frito')
                    break
            case _:
                print('Sala inexistente.')
                continue
