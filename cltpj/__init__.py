"""CLT x PJ - calcula o salário líquido com CLT e o faturamento mensal como PJ pelo Simples Nacional.

Calcula os impostos pagos em contratações pela CLT.
Calcula o imposto de uma empresa pelo Simples Nacional.
"""

from .clt import CLT
from .pj_simples import PJSimples

__all__ = ["PJSimples", "CLT"]
