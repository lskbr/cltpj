from rich import print
from rich.table import Table

from .optimiza import acha_clt, acha_pj


def constroi_tabela(pf, pj):
    pf = str(pf).splitlines()
    pj = str(pj).splitlines()
    tabela = Table(title="CLT x PJ")
    tabela.add_column("CLT")
    tabela.add_column("PJ")

    if len(pf) < len(pj):
        pf.extend(["" for _ in range(len(pj) - len(pf))])
    if len(pj) < len(pf):
        pj.extend(["" for _ in range(len(pf) - len(pj))])
    for pf_c, pj_c in zip(pf, pj, strict=True):
        tabela.add_row(pf_c, pj_c)
    return tabela


while True:
    print("0 - Sai")
    print("1 - Achar faturamento PJ Simples a partir de salário CLT")
    print("2 - Achar salário CLT equivalente a proposta PJ\n")
    try:
        opcao: int | None = int(input("Escolha uma operação: ").strip())
        if opcao == 1:
            salario_clt = float(input("Salário CLT: "))
            faturamento, pf, pj = acha_pj(salario_clt)
            print(
                f"CLT R${salario_clt:12,.2f} equivale a um faturamento mensal PJ R${faturamento:12,.2f}",
            )
        elif opcao == 2:  # noqa: PLR2004
            faturamento = float(input("Faturamento como PJ Simples: "))
            _, pf, pj = acha_clt(faturamento)
            print(
                f"Um faturamento PJ Simples R${faturamento:12,.2f} equivale a salário CLT R${pf.salario:12,.2f}",
            )
        elif opcao == 0:
            break
        else:
            raise ValueError("Opção inválida")  # noqa: TRY301
        print(constroi_tabela(pf, pj))
    except ValueError:
        print("[red]Opção inválida")
        opcao = None
    except Exception as erro:
        print(f"[red]Erro: {erro}")
