import os

import numpy as np
import pandas as pd
import requests
from scipy.stats import beta, norm


def bayesian_inference(groups, acc_clicks, acc_visits):
    qtd_amostas = acc_clicks[0].size
    resultados = []
    for i in range(acc_clicks[0].size - 1):
        acc_clicks_A = acc_clicks[0][i]
        acc_clicks_B = acc_clicks[1][i + 1]
        acc_visits_A = acc_visits[0][i]
        acc_visits_B = acc_visits[1][i + 1]

        # Mean and Variance
        media_a, variancia_a = media_variance(acc_clicks_A, acc_visits_A)
        media_b, variancia_b = media_variance(acc_clicks_B, acc_visits_B)

        # Amostras da distribuição Normal
        distruibuicao_normal_a = amostra_normal(media_a, variancia_a, qtd_amostas)
        distruibuicao_normal_b = amostra_normal(media_b, variancia_b, qtd_amostas)

        # Beta Probability Density Function of page
        probabilidade_beta_a = probabilidade_beta(
            distruibuicao_normal_a, acc_clicks_A, acc_visits_A
        )
        probabilidade_beta_b = probabilidade_beta(
            distruibuicao_normal_b, acc_clicks_B, acc_visits_B
        )

        # Normal Probability Density Function of page
        probabilidade_normal_a = probabilidade_normal(
            distruibuicao_normal_a, media_a, variancia_a
        )
        probabilidade_normal_b = probabilidade_normal(
            distruibuicao_normal_b, media_b, variancia_b
        )

        # beta / Normal
        constante_normalizacao = (probabilidade_beta_a * probabilidade_beta_b) / (
            probabilidade_normal_a * probabilidade_normal_b
        )

        # Somente valores onde o B é maior do que A
        valores_maior_b = constante_normalizacao[
            distruibuicao_normal_b >= distruibuicao_normal_a
        ]

        # Propabilidade de B ser melhor do que A
        probabilidade = (1 / qtd_amostas) * np.sum(valores_maior_b)

        # Erro ao assumir B melhor do que A
        expected_loss_A = (1 / qtd_amostas) * np.sum(
            (
                (distruibuicao_normal_b - distruibuicao_normal_a)
                * constante_normalizacao
            )[distruibuicao_normal_b >= distruibuicao_normal_a]
        )
        expected_loss_B = (1 / qtd_amostas) * np.sum(
            (
                (distruibuicao_normal_a - distruibuicao_normal_b)
                * constante_normalizacao
            )[distruibuicao_normal_a >= distruibuicao_normal_b]
        )

        resultados.append([probabilidade, expected_loss_A, expected_loss_B])

    return resultados


def media_variance(acc_clicks, acc_visits):
    media, variance = beta.stats(
        a=1 + acc_clicks, b=1 + acc_visits - acc_clicks, moments="mv"
    )

    return media, variance


def amostra_normal(media, variancia, qtd_amostas):
    return np.random.normal(
        loc=media, scale=1.25 * np.sqrt(variancia), size=qtd_amostas
    )


def probabilidade_beta(distruibuicao_normal, acc_clicks, acc_visits):
    return beta.pdf(
        distruibuicao_normal, a=1 + acc_clicks, b=1 + acc_visits - acc_clicks
    )


def probabilidade_normal(distruibuicao_normal, media, variancia):
    return norm.pdf(distruibuicao_normal, loc=media, scale=1.25 * np.sqrt(variancia))


def get_chart_data():
    groups = ["treatment", "control"]
    data = load_data()

    data = values_not_exists(data, groups)

    # Adjust the pivot table and column names to handle multiple groups
    data = data.reset_index().rename(columns={"index": "day"})
    data = data.pivot(index="day", columns="group", values=["click", "visit"]).fillna(0)

    data.columns = [f"{col}_{group}" for group in groups for col in ["click", "visit"]]
    data = data.reset_index(drop=True)

    # Calculate accumulated values for each group
    for group in groups:
        data[f"acc_visits_{group}"] = data[f"visit_{group}"].cumsum()
        data[f"acc_clicks_{group}"] = data[f"click_{group}"].cumsum()
    bayesian = pd.DataFrame()
    colunas = [
        "Probabilidade de B ser melhor que A",
        "Risco de Escolher A",
        "Risco de Escolher B",
    ]

    acc_clicks = [data[f"acc_clicks_{group}"] for group in groups]
    acc_visits = [data[f"acc_visits_{group}"] for group in groups]

    # Chama a função bayesian_inference passando os dados acumulados
    bayesian[colunas] = bayesian_inference(groups, acc_clicks, acc_visits)

    return bayesian


def load_data():
    url = os.getenv("WEB_URL", "http://localhost:5000")
    url = url + "/dados"
    r = requests.get(url)

    data = pd.DataFrame(r.json(), columns=r.json()[0].keys())
    return data


def values_not_exists(data, groups):
    for group in groups:
        if not data["group"].isin([group]).any():
            data = add_default_row(data, group)
    return data


def add_default_row(data, group_value):
    default_row = pd.DataFrame({"click": [0], "visit": [0], "group": [group_value]})
    return pd.concat([data, default_row])
