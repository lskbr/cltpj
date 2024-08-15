from .impostos import ir, inss_prolabore, simples_III_V


class PJ_Simples:
    def __init__(self, faturamento, prolabore, contador=200.0):
        self.faturamento = faturamento
        self.faturamento_anual = faturamento * 12
        self.prolabore = prolabore

        self.prolabore_inss = inss_prolabore(prolabore)
        self.contador = contador

        self.simples, self.fator_r = simples_III_V(self.prolabore, self.faturamento)

        self.despesas = self.contador + self.prolabore

        self.base_ir_prolabore = self.prolabore - self.prolabore_inss
        self.ir_prolabore = ir(self.base_ir_prolabore)

        self.socio_liquido = self.prolabore - self.prolabore_inss - self.ir_prolabore

        self.saldo_empresa = self.faturamento - self.despesas - self.simples

        self.saldo_empresa_socio = self.saldo_empresa + self.socio_liquido
        self.perda = faturamento - self.saldo_empresa_socio

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
