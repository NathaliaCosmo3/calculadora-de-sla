# Calculadora de SLA

## Baixar e abrir no navegador

**[Baixar projeto em ZIP](https://github.com/NathaliaCosmo3/calculadora-de-sla/archive/refs/heads/main.zip)**

1. Extraia o ZIP. No Windows, clique com o botão direito no arquivo e escolha **Extrair Tudo**.
2. Na pasta extraída, abra `index.html` com duplo clique. A interface funciona offline e dispensa instalação.

Use **Carregar exemplo** para ver o cálculo de 02/12/2026, os dias contados e o histórico da sessão. Você pode informar feriados no formato AAAA-MM-DD, um por linha.

## Versão em Python para terminal


Calcula o vencimento de um prazo de atendimento a partir da data de abertura e de uma quantidade de dias úteis. A contagem começa no dia seguinte e pula sábados, domingos e feriados informados no comando.

## Como executar

Com Python 3, rode na pasta do projeto:

```shell
python sla.py 2026-11-27 2 --feriado 2026-11-30
```

Neste exemplo fictício, o vencimento é **02/12/2026**. Repita `--feriado` para informar mais de uma data. A calculadora trabalha com dias inteiros e usa o calendário informado na execução.

Projeto de portfólio desenvolvido com assistência de IA.
