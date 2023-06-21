# A senha precisa ter, no mínimo:
# 1 letra maiúscula;
# 1 letra minúscula;
# 1 caractere especial
# 1 número;
# 8 a 12 caracteres totais
# Obs: Esse gerador poderia ter várias formas de fazer, e várias condições diferentes.
# Essa foi apenas uma das formas escolhida por mim.
# OBS_2: nem todos os caracteres especiais foram incluídos nos values que preenchem o dicionário.

def gerador_de_senhas():
    """
    Nessa função, são geradas senhas aleatórias, com caractere especial, números, letras maiúsculas e minúsculas.
    :return: retorna a senha gerada aleatoriamente.
    """
    from random import choice, choices, shuffle, randint

    caracteres = {
        'numéricos': ['0', '1', '2', '3', '4', '5',
                      '6', '7', '8', '9'],
        'especiais': ['!', '@', '#', '$', '%', '*'],
        'letras': ['q', 'w', 'e', 'r', 't', 'y', 'i',
                   'o', 'p', 'a', 's', 'd', 'f', 'g',
                   'h', 'j', 'k', 'l', 'ç', 'z', 'x',
                   'c', 'v', 'b', 'n', 'm']
    }
    senha = choices(caracteres['numéricos'], k=randint(3, 4))
    senha += choices(caracteres['letras'], k=randint(3, 4))
    for letra in range(randint(1, 4)):
        senha += choice(caracteres['letras']).upper()  # Não foi possível utilizar o .upper() com o choices,
        # por isso, foi criado um loop com tamanho aleatório para transformar em maiúsculas.
    senha += choices(caracteres['especiais'], k=randint(1, 4))
    shuffle(senha)  # aqui a senha é embaralhada, para que não fique sempre com um padrão bem parecido.
    senha_final = ''
    for c in senha:
        senha_final += c
    return senha_final[0:randint(8, 12)]  # Independente de quantos caracteres foram gerados anteriormente,
    # são retornados entre 8 e 12 (escolhido aleatoriamente também).


senha = gerador_de_senhas()
print(f'A senha gerada foi: {senha}')
print(f'O tamanho da senha é {len(senha)}')
