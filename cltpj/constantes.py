#
# Valores atualizados em 2024-08-16
#

# Alíquota do FGTS - Fundo de Garantia por Tempo de Serviço
FGTS = 0.08
# Multa sobre o saldo do FGTS quando o trabalhador é demitido
# sem justa causa
MULTA_FGTS = 0.4

# Tipo das tabelas de faixas
TIPO_ITEM = list[float | None]
TIPO_TABELA_FAIXA = list[TIPO_ITEM]

# Imposto de Renda Pessoa Física - IRPF
# https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2024
IMPOSTO_DE_RENDA: TIPO_TABELA_FAIXA = [
    [2_259.20, 0],
    [2_826.65, 0.075],
    [3_751.06, 0.15],
    [4_664.68, 0.225],
    [None, 0.275],
]

# Desconto do IRPF por dependente
# https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/imposto-de-renda/dirpf/deducoes/29-despesa-com-dependente
DESCONTO_IR_POR_DEPENDENTE = 2_275.08 / 12  # Converte a redução anual para mensal

# Seguro Social - INSS
# https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/tabela-de-contribuicao-mensal
INSS: TIPO_TABELA_FAIXA = [
    [1_412.00, 0.075],
    [2_666.68, 0.09],
    [4_000.03, 0.12],
    [7_786.02, 0.14],
]

# Simples Nacional - Tabela do Anexo III

ANEXO_III: TIPO_TABELA_FAIXA = [
    [180_000, 0.06],
    [360_000, 0.112],
    [720_000, 0.135],
    [1_800_000, 0.16],
    [3_600_000, 0.21],
    [4_800_000, 0.33],
]

# Simples Nacional - Tabela do Anexo V
ANEXO_V: TIPO_TABELA_FAIXA = [
    [180_000, 0.155],
    [360_000, 0.18],
    [720_000, 0.195],
    [1_800_000, 0.205],
    [3_600_000, 0.23],
    [4_800_000, 0.305],
]


def garante_float(v: float | None):
    if isinstance(v, int):
        return float(v)
    elif isinstance(v, float):  # noqa: RET505
        return v
    raise ValueError(f"Valor {v} tem que ser float")


# Faturamento anual máximo para estar no simples
MAX_SIMPLES_ANUAL: float = garante_float(ANEXO_V[-1][0])

# INSS sobre o prolabore
INSS_PROLABORE: float = 0.11

# Valor mínimo a considerar para pagar o INSS (salário mínimo)
MIN_INSS: float = garante_float(INSS[0][0])

# Valor máximo a pagar o INSS (teto)
MAX_INSS: float = garante_float(INSS[-1][0])

# Relação entre o prolabore e o faturamento para escolher o anexo do simples
FATOR_R: float = 0.28

# Custo mensal com contador
CUSTO_CONTADOR_DEFAULT: float = 200.0
