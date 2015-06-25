#!/usr/bin/env python
from __future__ import print_function, division

from collections import Counter

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


LOANS_DATA_URL = 'https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv'


def load_data():
    return pd.read_csv(LOANS_DATA_URL)
 

def clean_data(df):
    df.dropna(inplace=True)


def data_frequency(df):
    return Counter(df['Open.CREDIT.Lines'])


def graph_loans(freq):
    plt.figure()
    plt.bar(freq.keys(), freq.values(), width=1)
    plt.show()


def chi_square_test(freq):
    chi, p = stats.chisquare(freq.values())
    print(chi)
    print(p)


def chi_calc(freq):
    """
    chi-square calculation from first principles
    Assumed that expected distribution is flat.
    """
    n = len(freq)
    total = sum(freq.values())
    expected = total / n
    chi_iter = (x - expected for x in freq.values())
    print(sum(c * c / expected for c in chi_iter))


def main():
    loansData = load_data()
    clean_data(loansData)
    freq = data_frequency(loansData)
    graph_loans(freq)
    chi_square_test(freq)
    print(len(freq))
    print(freq.most_common(1))


if __name__ == '__main__':
    main()
