# Calculadora de SLA

## Abrir a versão visual

1. Abra o [arquivo index.html](https://github.com/NathaliaCosmo3/calculadora-de-sla/blob/main/index.html).
2. Na barra acima do código, clique no ícone de download (**Download raw file**).
3. Na pasta **Downloads**, abra `index.html` com dois cliques. Ele funciona offline no Chrome ou Edge, sem instalar Python.

**[Baixar todos os arquivos em ZIP](https://github.com/NathaliaCosmo3/calculadora-de-sla/archive/refs/heads/main.zip)**

Clique em **Carregar exemplo** para calcular um vencimento com feriado. O painel mantém os dez cálculos mais recentes neste navegador e exporta o histórico em CSV.

## Versão em Python para terminal

Calcula o vencimento de um prazo de atendimento a partir da data de abertura e de uma quantidade de dias úteis. A contagem começa no dia seguinte e pula sábados, domingos e feriados informados no comando.

## Como executar

Com Python 3, rode na pasta do projeto:

```shell
python sla.py 2026-11-27 2 --feriado 2026-11-30
```

Neste exemplo fictício, o vencimento é **02/12/2026**. Repita `--feriado` para informar mais de uma data. A calculadora trabalha com dias inteiros e usa o calendário informado na execução.

Projeto de portfólio desenvolvido com assistência de IA.
