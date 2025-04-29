import random

def escolher_palavra():
    palavras = ['banana', 'abacaxi', 'computador', 'python', 'inteligencia', 'desenvolvimento']
    return random.choice(palavras).lower()

def mostrar_palavra(palavra, letras_corretas):
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra])

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    print("Bem-vindo ao jogo da Forca!")

    while tentativas > 0:
        print("\nPalavra:", mostrar_palavra(palavra_secreta, letras_corretas))
        print("Letras erradas:", ', '.join(letras_erradas))
        print(f"Tentativas restantes: {tentativas}")

        chute = input("Digite uma letra: ").lower()

        if not chute.isalpha() or len(chute) != 1:
            print("Por favor, digite apenas uma letra.")
            continue

        if chute in letras_corretas or chute in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if chute in palavra_secreta:
            letras_corretas.append(chute)
            print("Boa! Você acertou uma letra.")
        else:
            letras_erradas.append(chute)
            tentativas -= 1
            print("Ops! Essa letra não está na palavra.")

        if all(letra in letras_corretas for letra in palavra_secreta):
            print("\nParabéns! Você venceu! A palavra era:", palavra_secreta)
            break
    else:
        print("\nVocê perdeu! A palavra era:", palavra_secreta)

# Início do jogo
jogar_forca()

