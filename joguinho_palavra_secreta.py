'''
Faça um jogo para o usuáro adivinhar qual a palavra secreta.
    Você vai propor uma palavra secreta qualquer e vai dar a
possibilidade para o usuário digitar apenas uma letra.
    Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
'''
import os

palavra_secreta = 'chocolate'.lower() #variável que guarda a palavra secreta
letras_acertadas = ''
numero_tentativas = 0

while True:
    
    letra_digitada = input('Digite apenas uma letra: ').lower()
    numero_tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada: {}'.format(palavra_formada))


    if palavra_formada == palavra_secreta:
        os.system('cls') # cls é o comando que limpa o terminal (verificar o comando que limpa o terminal do sistema operacional utilizado, e substitui-lo entre as aspas.)
        print('VOCÊ GANHOU, PARABÉNS!')
        print('A palavra era: {}'.format(palavra_secreta))
        print('Número de tentativas: {}'.format(numero_tentativas))
        letras_acertadas = ''
        numero_tentativas = 0
        sair = input('Digite "S" ou "Sair" para sair, ou digite "R" ou "Reiniciar" para jogar novamente: ').lower()
        if sair == 'sair' or sair == 's':
            break
        elif sair == 'reiniciar' or sair == 'r':
            continue