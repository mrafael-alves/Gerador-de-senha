import secrets
import string

"""
Gerador de senha aleatória.

REQUISISTOS:
Entrada
- Quantidade de caracteres como ENTRADA da função

Saída
- Deve conter pelo menos 1 caractere especial
- Deve conter pelo menos 1 letra maiúscula
- Deve conter 2 dígitos

"""

# Definição dos caracteres que irão compor a senha
maiusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase
numeros = string.digits
simbolos = string.punctuation

alfabeto = maiusculas + minusculas + numeros + simbolos


# Função geradora de senha aleatória de tamanho especificado na entrada
def gera_senha(max_len):
    senha_len = max_len
    senha = ''
    while len(senha) != max_len:
        for i in range(senha_len):
            senha += ''.join(secrets.choice(alfabeto))

        if (any(char in simbolos for char in senha)) and \
                (sum(char in numeros for char in senha) == 2) and \
                (any(char in maiusculas for char in senha)):
            return senha
        else:
            senha = ''


if __name__ == '__main__':
    gerador = gera_senha(8)
    print(f'Senha: {gerador} \nCaracteres: {len(gerador)}')
