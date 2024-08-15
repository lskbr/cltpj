from .constantes import (
    IMPOSTO_DE_RENDA,
    INSS,
    ANEXO_III,
    ANEXO_V,
    MAX_INSS,
    INSS_PROLABORE,
    FATOR_R,
)


def calcula_faixa(valor: float, tabela) -> float:
    anterior = 0.0
    imposto = 0.0
    for teto, porcentagem in tabela:
        if teto is None or valor <= teto:
            imposto += (valor - anterior) * porcentagem
            break
        else:
            imposto += (teto - anterior) * porcentagem
            if valor < teto:
                break
            anterior = teto + 0.01
    return imposto


def arredonda(v, casas=2):
    if v is float or v is int:
        return round(v, casas)
    else:
        return v


def ir(base: float) -> float:
    return arredonda(calcula_faixa(base, IMPOSTO_DE_RENDA), 2)


def inss(salario: float) -> float:
    return arredonda(calcula_faixa(salario, INSS), 2)


# Simples Nacional
def anexo_iii(faturamento):
    return arredonda(calcula_faixa(faturamento * 12, ANEXO_III), 2)


def anexo_v(faturamento):
    return arredonda(calcula_faixa(faturamento * 12, ANEXO_V), 2)


def simples_III_V(prolabore, faturamento):
    fator_r = prolabore / faturamento

    if fator_r <= FATOR_R:
        simples = anexo_v(faturamento)
    else:
        simples = anexo_iii(faturamento)

    return simples / 12, fator_r


# Impostos sobre o prolabore
def inss_prolabore(prolabore):
    return min(prolabore * INSS_PROLABORE, MAX_INSS)
