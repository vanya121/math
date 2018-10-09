#!usr/bin/python
import pandas as pd


def compute_roi(
    coins: pd.DataFrame, investments: dict, start_date: str, end_date: str
):
    answer = 0
    sum_inv = 0
    for key in investments:
        coi = coins[(coins['symbol'] == key) & ((coins['date'] == start_date) | (coins['date'] == end_date))]
        seq = coi['price']
        answer = answer + (investments[key] * (seq[end_date] - seq[start_date]) / seq[start_date])
        sum_inv = sum_inv + investments[key]
    return answer / sum_inv
