import argparse
from datetime import date, timedelta


def calcular_vencimento(inicio, dias_uteis, feriados):
    vencimento = inicio
    while dias_uteis:
        vencimento += timedelta(days=1)
        if vencimento.weekday() < 5 and vencimento not in feriados:
            dias_uteis -= 1
    return vencimento


def main():
    parser = argparse.ArgumentParser(description="Calcula o prazo em dias úteis.")
    parser.add_argument("abertura", type=date.fromisoformat, help="Data AAAA-MM-DD")
    parser.add_argument("dias", type=int, help="Quantidade de dias úteis")
    parser.add_argument("--feriado", type=date.fromisoformat, action="append", default=[])
    args = parser.parse_args()
    if args.dias < 1:
        parser.error("Informe pelo menos um dia útil.")
    try:
        vencimento = calcular_vencimento(args.abertura, args.dias, set(args.feriado))
    except OverflowError:
        parser.error("O prazo ultrapassa o intervalo de datas suportado.")
    print(f"Vencimento: {vencimento:%d/%m/%Y}")


if __name__ == "__main__":
    main()
