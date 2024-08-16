from .constantes import FGTS, MULTA_FGTS
from .impostos import imposto_de_renda_pessoa_fisica, inss


class CLT:
    def __init__(self, salario: float, dependentes: int = 0):
        self.salario = salario
        self.seguro_social = inss(salario)
        self.base_ir = self.salario - self.seguro_social
        self.irpf = imposto_de_renda_pessoa_fisica(self.base_ir, dependentes)

        self.impostos = self.irpf + self.seguro_social

        self.ferias = self.salario / 12 / 3
        self.decimo_terceiro = self.salario / 12

        self.fgts = self.salario * FGTS
        self.fgts_ferias = self.ferias * FGTS
        self.fgts_13 = self.decimo_terceiro * FGTS

        self.total_fgts = self.fgts + self.fgts_ferias + self.fgts_13

        self.aviso_previo = self.total_fgts * MULTA_FGTS

        self.seguro_social_ferias = (
            0  # Mudança de jurisprudência (inss(salario * 1.3) - seguro_social) / 12
        )
        self.seguro_social_13 = (inss(salario * 2) - self.seguro_social) / 12

        self.ir_ferias = (
            imposto_de_renda_pessoa_fisica(self.salario * 1.3) - self.irpf
        ) / 12
        self.base_decimo_terceiro = self.salario * 2 - inss(self.salario * 2)
        self.ir_decimo_terceiro = (
            imposto_de_renda_pessoa_fisica(self.base_decimo_terceiro) - self.irpf
        ) / 12

        self.indireto = (
            self.fgts
            + self.ferias
            + self.aviso_previo
            + self.fgts_ferias
            + self.fgts_13
            + self.decimo_terceiro
            - self.seguro_social_ferias
            - self.seguro_social_13
            - self.ir_ferias
            - self.ir_decimo_terceiro
        )

        self.mensal = self.salario - self.impostos + self.indireto

    def __repr__(self):
        return f"<CLT salário={self.salario} mensal={self.mensal}>"

    def __str__(self):
        return f"""
    Salário       {self.salario:12,.2f}

    Impostos
    INSS        + {self.seguro_social:12,.2f}
    IR          + {self.irpf:12,.2f}
                ==============
                  {self.impostos:12,.2f}

    Benefícios indiretos
    FGTS                               + {self.fgts:12,.2f}
    Férias                             + {self.ferias:12,.2f}
    FGTS Férias                        + {self.fgts_ferias:12,.2f}
    Aviso prévio                       + {self.aviso_previo:12,.2f}
    Décimo Terceiro                    + {self.decimo_terceiro:12,.2f}
    FGTS Décimo Terceiro               + {self.fgts_13:12,.2f}
    INSS Férias                        - {self.seguro_social_ferias:12,.2f}
    INSS Décimo Terceiro               - {self.seguro_social_13:12,.2f}
    IRPF Férias                        - {self.ir_ferias:12,.2f}
    IRPF Décimo Terceiro               - {self.ir_decimo_terceiro:12,.2f}
                                       ==============
                                         {self.indireto:12,.2f}

    Salário                {self.salario:12,.2f}
    Impostos             - {self.impostos:12,.2f}
                         ==============
    Líquido                {self.mensal-self.indireto:12,.2f}
    Benefícios           + {self.indireto:12,.2f}
                         ==============
    Líquido + Benefícios   {self.mensal:12,.2f}
            """
