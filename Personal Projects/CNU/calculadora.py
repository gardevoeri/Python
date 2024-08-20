# Calculadora para verificar a nota das provas objetivas por cargo concorrido
def calc(acertos, vaga):
    gerais = (acertos[0] * 100) / 20
    espc = (
        (acertos[1] * vaga[1])
        + (acertos[2] * vaga[2])
        + (acertos[3] * vaga[3])
        + (acertos[4] * vaga[4])
        + (acertos[5] * vaga[5])
    )

    if vaga[0] == 1:
        gerais = gerais * 0.2
        espc = espc * 0.5
        corte = 28
    elif vaga[0] == 2:
        gerais = gerais * 0.25
        espc = espc * 0.5
        corte = 30
    elif vaga[0] == 3:
        gerais = gerais * 0.25
        espc = espc * 0.55
        corte = 32

    nota = gerais + espc
    return nota, corte


# Criar funções para calcular de acordo com cada tabela de órgão


# Valores da prova
objetiva = [15, 5, 5, 5, 5, 4]

# Criar valores por órgão de cada peso do eixo
cargos = [
    [
        "B2-03-A",
        "IBGE - Analista de Planejamento: Desen. de Tec. da Informação",
        [3, 1, 1, 2, 5, 1],
    ],
    [
        "B2-03-B",
        "IBGE - Analista de Planejamento: Infra e Sup. Tec. Informação",
        [3, 1, 1, 5, 1, 2],
    ],
    [
        "B2-03-E",
        "IBGE - Tecnologista em Informações: Ciência de Dados",
        [3, 1, 1, 2, 2, 4],
    ],
    [
        "B2-03-G",
        "IBGE - Tecnologista em Informações: Métodos Quantitativos",
        [3, 1, 2, 1, 1, 5],
    ],
    [
        "B2-05-A",
        "INEP - Pesquisador Tecnologista: Qualquer área",
        [1, 1, 2, 1, 1, 5],
    ],
    [
        "B2-07-A",
        "MCTI - Analista em Ciencia e Tecnologia: Ciência de Dados",
        [1, 2, 2, 1, 1, 4],
    ],
    [
        "B2-07-B",
        "MCTI - Analista em Ciencia e Tecnologia: Tecnologia da Informação",
        [1, 2, 3, 3, 1, 1],
    ],
    [
        "B2-08-A",
        "MGI - Analista ATI: Tecnologia da Informação",
        [1, 1, 1, 3, 3, 2],
    ],
    [
        "B2-08-B",
        "MGI - Analista ATPS: Tecnologia da Informação",
        [1, 2, 3, 1, 1, 3],
    ],
    [
        "B2-08-C",
        "MGI - Especialista Políticas Públicas: Qualquer Área",
        [1, 4, 3, 1, 1, 1],
    ],
    ["B2-03-A", "MS - Tecnologista: Tecnologia da Informação", [1, 1, 1, 3, 3, 2]],
    [
        "B2-03-A",
        "PREVIC - Analista Administrativo: Tecnologia da Informação",
        [2, 1, 1, 3, 3, 2],
    ],
]


for cargo in cargos:
    notas_org = calc(objetiva, cargo[2])
    print(cargo[1])
    print("Nota Estimada: ", notas_org[0])
    print("Corte: ", notas_org[1])
    print()


# lista1 = [15, 5, 5, 5, 5, 4]
# lista2 = [1, 4, 3, 1, 1, 1]
# test = calc(lista1, lista2)

# print(test[0])
# print()
# print(test[1])
