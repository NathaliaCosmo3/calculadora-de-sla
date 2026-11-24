# Calculadora de SLA

Calcula o vencimento de um prazo de atendimento a partir da data de abertura e de uma quantidade de dias úteis. A contagem começa no dia seguinte e pula sábados, domingos e feriados informados no comando.

## Como executar

Com Python 3, rode na pasta do projeto:

```shell
python sla.py 2026-11-27 2 --feriado 2026-11-30
```

Neste exemplo fictício, o vencimento é **02/12/2026**. Repita `--feriado` para informar mais de uma data. A calculadora trabalha com dias inteiros e usa o calendário informado na execução.

Projeto de portfólio desenvolvido com assistência de IA.
