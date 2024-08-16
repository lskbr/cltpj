# CLT x PJ

Script para gerar uma estimativa entre o salário líquido como CLT x Pessoa Jurídica.

Este script pode ser usado para simular o salário líquido entre uma contratação CLT x PJ pelo Simples.

Como é uma estimativa, vários detalhes foram simplificados:

- Vale transporte
- Vale refeição

# Usando

Versão interativa:

```
python -m cltpj
```

Exemplo:

```
0 - Sai
1 - Achar faturamento PJ Simples a partir de salário CLT
2 - Achar salário CLT equivalente a proposta PJ

Escolha uma operação: 1
Salário CLT: 5000
CLT R$    5,000.00 equivale a um faturamento mensal PJ R$    6,492.20
                                                       CLT x PJ
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ CLT                                                   ┃ PJ                                                         ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│                                                       │                                                            │
│     Salário           5,000.00                        │     Faturamento Anual            77,904.00                 │
│                                                       │                                                            │
│     Impostos                                          │     Receitas/Despesas mensais:                             │
│     INSS        +       518.82                        │     Faturamento                   6,492.00                 │
│     IR          +       345.49                        │     Contador                -       200.00                 │
│                 ==============                        │     Prolabore               -     1,412.00                 │
│                         864.31                        │     Simples                 -     1,006.26 (       15.50%) │
│                                                       │                             ==============                 │
│     Benefícios indiretos                              │     Saldo Empresa                 3,873.74                 │
│     FGTS                               +       400.00 │                                                            │
│     Férias                             +       138.89 │     Fator-R (simples)                 0.22                 │
│     FGTS Férias                        +        11.11 │                                                            │
│     Aviso prévio                       +       177.78 │     Sócio                                                  │
│     Décimo Terceiro                    +       416.67 │     Prolabore               +     1,412.00                 │
│     FGTS Décimo Terceiro               +        33.33 │     INSS sobre o prolabore  -       155.32                 │
│     INSS Férias                        -         0.00 │     IR Prolabore            -         0.00                 │
│     INSS Décimo Terceiro               -        32.50 │                             ==============                 │
│     IRPF Férias                        -        45.50 │     Saldo Sócio                   1,256.68                 │
│     IRPF Décimo Terceiro               -       104.88 │                                                            │
│                                        ============== │     Saldo Empresa + Sócio         5,130.42                 │
│                                                994.89 │                                                            │
│                                                       │                                                            │
│     Salário                    5,000.00               │                                                            │
│     Impostos             -       864.31               │                                                            │
│                          ==============               │                                                            │
│     Líquido                    4,135.69               │                                                            │
│     Benefícios           +       994.89               │                                                            │
│                          ==============               │                                                            │
│     Líquido + Benefícios       5,130.59               │                                                            │
│                                                       │                                                            │
└───────────────────────────────────────────────────────┴────────────────────────────────────────────────────────────┘
0 - Sai
1 - Achar faturamento PJ Simples a partir de salário CLT
2 - Achar salário CLT equivalente a proposta PJ

Escolha uma operação: 2
Faturamento como PJ Simples: 10000
Um faturamento PJ Simples R$   10,000.00 equivale a salário CLT R$    8,464.00
                                                       CLT x PJ
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ CLT                                                   ┃ PJ                                                         ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│                                                       │                                                            │
│     Salário           8,464.00                        │     Faturamento Anual           120,000.00                 │
│                                                       │                                                            │
│     Impostos                                          │     Receitas/Despesas mensais:                             │
│     INSS        +       908.86                        │     Faturamento                  10,000.00                 │
│     IR          +     1,181.65                        │     Contador                -       200.00                 │
│                 ==============                        │     Prolabore               -     1,412.00                 │
│                       2,090.51                        │     Simples                 -     1,550.00 (       15.50%) │
│                                                       │                             ==============                 │
│     Benefícios indiretos                              │     Saldo Empresa                 6,838.00                 │
│     FGTS                               +       677.12 │                                                            │
│     Férias                             +       235.11 │     Fator-R (simples)                 0.14                 │
│     FGTS Férias                        +        18.81 │                                                            │
│     Aviso prévio                       +       300.94 │     Sócio                                                  │
│     Décimo Terceiro                    +       705.33 │     Prolabore               +     1,412.00                 │
│     FGTS Décimo Terceiro               +        56.43 │     INSS sobre o prolabore  -       155.32                 │
│     INSS Férias                        -         0.00 │     IR Prolabore            -         0.00                 │
│     INSS Décimo Terceiro               -         0.00 │                             ==============                 │
│     IRPF Férias                        -        79.02 │     Saldo Sócio                   1,256.68                 │
│     IRPF Décimo Terceiro               -       193.97 │                                                            │
│                                        ============== │     Saldo Empresa + Sócio         8,094.68                 │
│                                              1,720.76 │                                                            │
│                                                       │                                                            │
│     Salário                    8,464.00               │                                                            │
│     Impostos             -     2,090.51               │                                                            │
│                          ==============               │                                                            │
│     Líquido                    6,373.49               │                                                            │
│     Benefícios           +     1,720.76               │                                                            │
│                          ==============               │                                                            │
│     Líquido + Benefícios       8,094.24               │                                                            │
│                                                       │                                                            │
└───────────────────────────────────────────────────────┴────────────────────────────────────────────────────────────┘
```

# Calculando os impostos sobre o salário CLT

```
>>> from cltpj import CLT
>>> funcionario = CLT(salario=5000)
>>> funcionario
<CLT salário=5000 mensal=5130.585161736111>
>>> print(funcionario)

    Salário           5,000.00

    Impostos
    INSS        +       518.82
    IR          +       345.49
                ==============
                        864.31

    Benefícios indiretos
    FGTS                               +       400.00
    Férias                             +       138.89
    FGTS Férias                        +        11.11
    Aviso prévio                       +       177.78
    Décimo Terceiro                    +       416.67
    FGTS Décimo Terceiro               +        33.33
    INSS Férias                        -         0.00
    INSS Décimo Terceiro               -        32.50
    IRPF Férias                        -        45.50
    IRPF Décimo Terceiro               -       104.88
                                       ==============
                                               994.89

    Salário                    5,000.00
    Impostos             -       864.31
                         ==============
    Líquido                    4,135.69
    Benefícios           +       994.89
                         ==============
    Líquido + Benefícios       5,130.59
```

Exemplo com dependentes:

```
>>> from cltpj import CLT
>>> for d in range(5): print(repr(CLT(salario=10_000, dependentes=d)))
...
<CLT salário=10000 mensal=9523.898118680556>
<CLT salário=10000 mensal=9567.345827013889>
<CLT salário=10000 mensal=9610.793535347222>
<CLT salário=10000 mensal=9654.241243680555>
<CLT salário=10000 mensal=9697.688952013888>
```

# Calculando os impostos sobre o faturamento como PJ Simples

```
>>> from cltpj import PJ_Simples
>>> empresa = PJ_Simples(faturamento=12000, prolabore=6000, contador=180)
>>> empresa
<PJ_Simples faturamento=12000 prolabore=6000 saldo mensal=9867.5095>
>>> print(empresa)

    Faturamento Anual           144,000.00

    Receitas/Despesas mensais:
    Faturamento                  12,000.00
    Contador                -       180.00
    Prolabore               -     6,000.00
    Simples                 -       720.00 (        6.00%)
                            ==============
    Saldo Empresa                 5,100.00

    Fator-R (simples)                 0.50

    Sócio
    Prolabore               +     6,000.00
    INSS sobre o prolabore  -       660.00
    IR Prolabore            -       572.49
                            ==============
    Saldo Sócio                   4,767.51

    Saldo Empresa + Sócio         9,867.51
```
