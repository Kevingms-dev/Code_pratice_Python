funcionarios = {'ana': 25, 'bruno': 30, 'carla': 28}
funcionarios['gabriel'] = 35  # Adicionando um novo funcionário
funcionarios['ana'] = [25, 26]  # adiciona mais uma idade a ana
print(funcionarios)

def main():
    f = {}

    nome = input()
    while nome != '':
        salario = float(input())
        idade = int(input())
        f[nome] = [salario, idade]
        print(f'-' * 20)
        nome = input()
    exibe(f)

del funcionarios['carla']

def exibe(f: dict) -> None:
    #passa apenas pelas chaves do dicionário
    for chave, valor in f.items():
        print(f'Nome...: {chave}, Salário: {valor[0]}, Idade: {valor[1]}')

if __name__ == '__main__':
    main()