from scipy.optimize import Bounds, shgo

from .clt import CLT
from .constantes import MIN_INSS
from .pj_simples import PJSimples


def clt_pj(faturamento, vclt, prolabore_min=MIN_INSS):
    """Função objetivo para achar o valor do faturamento pj, a partir do valor clt."""
    pf = CLT(vclt)
    pj = PJSimples(faturamento, prolabore_min)
    return abs(pf.mensal - pj.saldo_empresa_socio)


def pj_clt(vclt, faturamento, prolabore_min=MIN_INSS):
    """Função objetivo para achar o valor do salário pago pela CLT a partir do faturamento da empresa."""
    pf = CLT(vclt)
    pj = PJSimples(faturamento, prolabore_min)
    return abs(pf.mensal - pj.saldo_empresa_socio)


def acha_pj(salario_clt, prolabore=MIN_INSS):
    """Retorna o faturamento equivalente a um salário CLT"""
    res = shgo(
        clt_pj,
        bounds=Bounds(salario_clt, salario_clt * 3),
        args=(salario_clt, prolabore),
    )
    pf = CLT(salario_clt)
    pj = PJSimples(round(res.x[0]), prolabore)
    return res.x[0], pf, pj


def acha_clt(faturamento, prolabore=MIN_INSS):
    """Retorna o salário pago pela CLT a partir de um faturamento como PJ Simples"""
    res = shgo(
        pj_clt,
        bounds=Bounds(MIN_INSS, faturamento * 2),
        args=(faturamento, prolabore),
    )
    pf = CLT(round(res.x[0]))
    pj = PJSimples(faturamento, prolabore)
    return res.x[0], pf, pj
