# Solicita os lados do triângulo
lado1 = float(input('Entre com o maior lado do triângulo: '))
lado2 = float(input('Entre com o segundo lado do triângulo: '))
lado3 = float(input('Entre com o terceiro lado do triângulo: '))

# Verifica se forma um triângulo válido
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):

    # Verifica o tipo de triângulo
    if (lado1 ** 2 == lado2 ** 2 + lado3 ** 2):  # condição1
        print('O triângulo é retângulo')
    elif (lado1 ** 2 < lado2 ** 2 + lado3 ** 2):  # condição2
        print('O triângulo é acutângulo')
    else:
        print('O triângulo é obtusângulo')

else:
    print('Os lados fornecidos não formam um triângulo válido!')