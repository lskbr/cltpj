from .constantes import MIN_INSS
from scipy.optimize import Bounds, shgo
from .pj_simples import PJ_Simples
from .clt import CLT


def clt_pj(faturamento, vclt, prolabore_min=MIN_INSS):
    pf = CLT(vclt)
    pj = PJ_Simples(faturamento, prolabore_min)
    return abs(pf.mensal - pj.saldo_empresa_socio)


def pj_clt(vclt, faturamento, prolabore_min=MIN_INSS):
    pf = CLT(vclt)
    pj = PJ_Simples(faturamento, prolabore_min)
    return abs(pf.mensal - pj.saldo_empresa_socio)


def acha_pj(salario_clt, prolabore=MIN_INSS):
    res = shgo(
        clt_pj,
        bounds=Bounds(salario_clt, salario_clt * 3),
        args=(salario_clt, prolabore),
    )
    pf = CLT(salario_clt)
    pj = PJ_Simples(round(res.x[0]), prolabore)
    return res.x[0], pf, pj


def acha_clt(faturamento, prolabore=MIN_INSS):
    res = shgo(
        pj_clt,
        bounds=Bounds(MIN_INSS, faturamento * 2),
        args=(faturamento, prolabore),
    )
    pf = CLT(round(res.x[0]))
    pj = PJ_Simples(faturamento, prolabore)
    return res.x[0], pf, pj
