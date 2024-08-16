from .constantes import (
    ANEXO_III,
    ANEXO_V,
    DESCONTO_IR_POR_DEPENDENTE,
    FATOR_R,
    IMPOSTO_DE_RENDA,
    INSS,
    INSS_PROLABORE,
    MAX_INSS,
)


def calcula_faixa(valor: float, tabela: list) -> float:
    """Função genérica para calcular faixas de impostos.
    A tabela é uma lista de listas.
    A primeira linha cobre a faixa entre 0 e o valor indicado.
    O primeiro valor é o fim da faixa e o segundo a porcentagem a aplicar na faixa.
    Se a última linha tem None como limite, este é considerado aberto.
    """
    anterior = 0.0
    imposto = 0.0
    for teto, porcentagem in tabela:
        if teto is None or valor <= teto:
            imposto += (valor - anterior) * porcentagem
            break
        imposto += (teto - anterior) * porcentagem
        if valor < teto:
            break
        anterior = teto + 0.01
    return imposto


def arredonda(v, casas=2):
    """Arredondamento simples para impressão.
    Verifica se é float ou int, pois os tipos do numpy usados pelo otimizador não suportam round.
    """
    if v is float or v is int:
        return round(v, casas)
    return v


def imposto_de_renda_pessoa_fisica(base: float, dependentes: int = 0) -> float:
    base = max(base - (dependentes * DESCONTO_IR_POR_DEPENDENTE), 0.0)
    return arredonda(calcula_faixa(base, IMPOSTO_DE_RENDA), 2)


def inss(salario: float) -> float:
    """Calcula o INSS sobre salário."""
    return arredonda(calcula_faixa(salario, INSS), 2)


# Simples Nacional
def anexo_iii(faturamento: float) -> float:
    return arredonda(calcula_faixa(faturamento * 12, ANEXO_III), 2)


def anexo_v(faturamento: float) -> float:
    return arredonda(calcula_faixa(faturamento * 12, ANEXO_V), 2)


def simples_iii_v(prolabore: float, faturamento: float) -> tuple[float, float]:
    """Escolhe a tabela do Anexo III ou do Anexo V em função da relação
    entre o prolabore e o faturamento da empresa (fator R).
    Quando o fator R é maior que 0.28, Anexo V
    """
    fator_r = prolabore / faturamento

    simples = anexo_v(faturamento) if fator_r <= FATOR_R else anexo_iii(faturamento)

    return simples / 12, fator_r


# Impostos sobre o prolabore
def inss_prolabore(prolabore: float) -> float:
    """Calcula o INSS sobre prolabore do sócio."""
    return min(prolabore * INSS_PROLABORE, MAX_INSS)
