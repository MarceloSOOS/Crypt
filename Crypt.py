# esse eh um algoritmo simples de criptografia, onde utiliza uma imagem como base para fazer calculos dos valores RGB e retornando um valor Pseudo aleatorio, 
# criei ele durante um periodo de estudos sobre a previsibilidade de numeros gerados por algoritmos.
# importante ter em mente que é apenas pra tirar algumas duvidas que eu tinha, o codigo em si eh cheio de falhas, pois não foi criado pra ser implementado em um sistema real

import cv2
import random
import string

# função para dividir um número em partes de 5 dígitos
def dividir_numero(numero):
    partes = []
    numero_str = str(int(numero))  # converte o número para inteiro e, em seguida, para string
    while len(numero_str) % 4 != 0:
        numero_str = '0' + numero_str  # adiciona zeros à esquerda para garantir que o número seja dividido em partes de 4
    for i in range(0, len(numero_str), 4):
        partes.append(numero_str[i:i+4])
    return partes

# função para gerar uma letra aleatória
def letra_aleatoria():
    return random.choice(string.ascii_uppercase)

# carrega a imagem
imagem = cv2.imread('C:\\Users\\Marcelo\\Desktop\\crypt\\VULCAO01.jpg')

# verifica se a imagem foi carregada corretamente
if imagem is None:
    print("Não foi possível abrir a imagem. Verifique o caminho do arquivo.")
else:
    # redimensiona a imagem para 1080x1080
    imagem_redimensionada = cv2.resize(imagem, (1080, 1080))

    # obtém as dimensões da imagem redimensionada
    altura, largura, _ = imagem_redimensionada.shape

    # inicializa a variável para armazenar a soma dos valores RGB
    soma_rgb = 0

    # itera sobre cada linha e coluna da imagem redimensionada
    for y in range(altura):
        for x in range(largura):
            # obtém o valor do pixel na posição (x, y)
            pixel = imagem_redimensionada[y, x]

            # soma os valores dos canais RGB do pixel
            soma_rgb += sum(pixel)

    # gera um número aleatório entre 50 e 254
    numero_aleatorio = random.randint(50, 254)

    # calcula o resultado da expressão
    resultado = (soma_rgb / numero_aleatorio) ** 2

    # divide o resultado em partes de 5 dígitos
    partes = dividir_numero(resultado)

    # adiciona uma letra aleatória em cada parte
    partes_com_letras = [parte + letra_aleatoria() for parte in partes]

    # imprime o resultado final
    resultado_final = '-'.join(partes_com_letras)
    print("Resultado final:", resultado_final)

    # libera a memória da imagem após o uso
    cv2.destroyAllWindows()
