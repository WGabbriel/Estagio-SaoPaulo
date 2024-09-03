import json


def calcular_faturamento(filename):
    with open(filename, "r") as file:
        dados = json.load(file)

    faturamentos = [dado["faturamento"] for dado in dados if dado["faturamento"] > 0]

    if not faturamentos:
        return "Não há dados de faturamento disponíveis."

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)

    dias_acima_da_media = sum(
        1 for faturamento in faturamentos if faturamento > media_faturamento
    )

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media,
    }


resultado = calcular_faturamento("faturamento.json")
print(resultado)
