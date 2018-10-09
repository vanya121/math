import pandas as pd
import math


def compute_volatility(
    coins: pd.DataFrame, investments: dict, start_date: str, end_date: str
):
    answer = 0
    for key in investments:
        D = 0
        coi = coins[(coins['symbol'] == key) & ((coins['date'] >= start_date) & (coins['date'] <= end_date))]
        seq1 = coi['price']
        seq = dict(seq1)
        cnt = 0
        M = 0
        for key1 in seq:
            M += seq[key1]
            cnt += 1
        M = M / cnt
        for key2 in seq:
            D += seq[key2] ** 2 - M ** 2
        D = math.sqrt(D / (cnt - 1))
        answer += D * investments[key] / seq1[start_date] * (seq1[end_date] - seq1[start_date])/abs(seq1[end_date] - seq1[start_date])
    return answer
