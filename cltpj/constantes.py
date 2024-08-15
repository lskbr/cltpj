# Aliquota do FGTS - Fundo de Garantia por Tempo de Serviço
FGTS = 0.08
# Multa sobre o saldo do FGTS quando o trabalhador é demitido
# sem justa causa
MULTA_FGTS = 0.4

# Imposto de Renda Pessoa Física - IRPF
# https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2024
IMPOSTO_DE_RENDA = [
    [2_259.20, 0],
    [2_826.65, 0.075],
    [3_751.06, 0.15],
    [4_664.68, 0.225],
    [None, 0.275],
]

# Seguro Social
# https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/tabela-de-contribuicao-mensal
INSS = [
    [1_412.00, 0.075],
    [2_666.68, 0.09],
    [4_000.03, 0.12],
    [7_786.02, 0.14],
]

# Simples Nacional
ANEXO_III = [
    [180_000, 0.06],
    [360_000, 0.112],
    [720_000, 0.135],
    [1_800_000, 0.16],
    [3_600_000, 0.21],
    [4_800_000, 0.33],
]

ANEXO_V = [
    [180_000, 0.155],
    [360_000, 0.18],
    [720_000, 0.195],
    [1_800_000, 0.205],
    [3_600_000, 0.23],
    [4_800_000, 0.305],
]

INSS_PROLABORE = 0.11
MIN_INSS = INSS[0][0]
MAX_INSS = INSS[-1][0]
FATOR_R = 0.28
