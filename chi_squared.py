#!/usr/bin/env python
from __future__ import print_function

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


def main():
    loansData = load_data()
    clean_data(loansData)
    freq = data_frequency(loansData)
    graph_loans(freq)
    chi_square_test(freq)


if __name__ == '__main__':
    main()
