from .constantes import CUSTO_CONTADOR_DEFAULT, MAX_SIMPLES_ANUAL, MIN_INSS
from .impostos import (
    imposto_de_renda_pessoa_fisica,
    inss_prolabore,
    simples_iii_v,
)


class PJSimplesError(Exception):
    pass


class PJSimples:
    def __init__(
        self,
        faturamento: float,
        prolabore: float = MIN_INSS,
        contador: float = CUSTO_CONTADOR_DEFAULT,
        dependentes: int = 0,
    ):
        self.faturamento = faturamento
        self.faturamento_anual = faturamento * 12
        if self.faturamento_anual > MAX_SIMPLES_ANUAL:
            raise PJSimplesError(
                f"Faturamento anual R${self.faturamento_anual} é superior ao máximo do simples {MAX_SIMPLES_ANUAL}",
            )
        self.prolabore = prolabore

        self.prolabore_inss = inss_prolabore(prolabore)
        self.contador = contador

        self.simples, self.fator_r = simples_iii_v(self.prolabore, self.faturamento)

        self.despesas = self.contador + self.prolabore

        self.base_ir_prolabore = self.prolabore - self.prolabore_inss
        self.ir_prolabore = imposto_de_renda_pessoa_fisica(
            self.base_ir_prolabore, dependentes=dependentes
        )

        self.socio_liquido = self.prolabore - self.prolabore_inss - self.ir_prolabore

        self.saldo_empresa = self.faturamento - self.despesas - self.simples

        self.saldo_empresa_socio = self.saldo_empresa + self.socio_liquido
        self.perda = faturamento - self.saldo_empresa_socio

    def __repr__(self):
        return (
            f"<PJ_Simples faturamento={self.faturamento} "
            f"prolabore={self.prolabore} saldo mensal={self.saldo_empresa_socio}>"
        )

    def __str__(self):
        return f"""
    Faturamento Anual         {self.faturamento_anual:12,.2f}

    Receitas/Despesas mensais:
    Faturamento               {self.faturamento:12,.2f}
    Contador                - {self.contador:12,.2f}
    Prolabore               - {self.prolabore:12,.2f}
    Simples                 - {self.simples:12,.2f} ({self.simples/self.faturamento*100:12,.2f}%)
                            ==============
    Saldo Empresa             {self.saldo_empresa:12,.2f}

    Fator-R (simples)         {self.fator_r:12,.2f}

    Sócio
    Prolabore               + {self.prolabore:12,.2f}
    INSS sobre o prolabore  - {self.prolabore_inss:12,.2f}
    IR Prolabore            - {self.ir_prolabore:12,.2f}
                            ==============
    Saldo Sócio               {self.socio_liquido:12,.2f}

    Saldo Empresa + Sócio     {self.saldo_empresa_socio:12,.2f}
        """
