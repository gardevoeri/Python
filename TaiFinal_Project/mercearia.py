from math import prod


listaProd = []


# Função de Cadastro de Produtos
def cadastrarProduto(c):
    print('Você selecionou a opção de Cadastrar Produto')
    print('Código do Produto {}'.format(c))
    nome = input('Por favor entre com o NOME do Produto: ')
    fabr = input('Por favor entre com o FABRICANTE do Produto: ')
    valor = float(input('Por favor entre com o valor (R$) do Produto: '))
    dicionarioProduto = {
        'cod': c,
        'nome': nome,
        'fabricante': fabr,
        'valor': valor}
    listaProd.append(dicionarioProduto.copy())

# Função Teste


def exibeDados(produto):
    print('-------------------------')
    for key, value in produto.items():
        print('{} : {}' .format(key, value))


# Função de Consulta de produto
def consultarProduto():
    while True:
        try:
            print('Você selecionou a opção de Consultar Produto')
            op_con = int(input('''Escolha a opção desejada:
            1 - Consultar todos os produtos
            2 - Consultar produtos por código
            3 - Consultar produtos por fabricante
            4 - Retornar
            '''))

            if op_con == 1:
                print('-------------------------')
                for produto in listaProd:
                    exibeDados(produto)
            elif op_con == 2:
                cc = int(input('Digite o CODIGO dos produto: '))
                for produto in listaProd:
                    if(produto['cod'] == cc):
                        exibeDados(produto)
            elif op_con == 3:
                fb = input('Digite o FABRICANTE dos produto: ')
                for produto in listaProd:
                    if(produto['fabricante'] == fb):
                        exibeDados(produto)
            elif op_con == 4:
                break
            else:
                print('Opção Inválida')
                continue
        except:
            print('Por favor digite um número inteiro!')


# Função para remover produto
def removerProduto():
    print('Você selecionou a opção remover produto')
    rem = int(input('Digite o código do produto a ser removido: '))
    for produto in listaProd:
        if(produto['cod'] == rem):
            listaProd.remove(produto)


# ****** CORPO DO PROGRAMA *****
# Não esquecer de colocar a RU
r_u = 4102632
print('Bem Vindo ao Controle de Estoque da Tainara dos S. S. Carlos. RU: {}'.format(r_u))

codigo_prod = 0
while True:
    try:
        menu = int(input('''Escolha a opção desejada:
        1 - Cadastrar produto
        2 - Consultar produto
        3 - Remover produto
        4 - Sair
        '''))

        if menu == 1:
            codigo_prod += 1
            cadastrarProduto(codigo_prod)
        elif menu == 2:
            consultarProduto()
        elif menu == 3:
            removerProduto()
        elif menu == 4:
            break
        else:
            print('Opção Inválida')
            continue
    except:
        print('Por favor digite um número inteiro!')
