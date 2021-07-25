import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import filtfilt
from scipy.signal import butter
from scipy.signal import find_peaks
import tkinter as tk
from tkinter import filedialog
import os
import matplotlib


matplotlib.rcParams['agg.path.chunksize'] = 10000


def Baseline(df, ampfr, avgnum):
    shft = sum(df['Ampl'][0:avgnum]) / avgnum
    df['Ampl'] = [ampfr * (x - shft) for x in df['Ampl']]

    return df


def Correction(df, cb, ca):
    b, a = butter(cb, ca)
    filt_df = filtfilt(b, a, df['Ampl'])
    df['Ampl'] = [df['Ampl'][i] - filt_df[i] for i in range(len(df))]

    return df


def Findpeak(df, hh, dis):
    peaks, _ = find_peaks(df['Ampl'], height=hh, distance=dis)
    np.diff(peaks)

    fpk_df = pd.DataFrame(columns=['Time', 'Ampl'])
    fpk_df['Time'] = df['Time'][peaks]
    fpk_df['Ampl'] = df['Ampl'][peaks]

    return fpk_df


def Mean(df, min, max):
    sel = []
    df.reset_index(inplace=True)
    for i in range(len(df)):
        if (min <= df['Time'][i] <= max):
            sel.append(df['Ampl'][i])
    area = sum(sel)
    mean = area/len(sel)

    return round(area, 3), round(mean, 3)


def Findtrend(df):
    ns = pd.DataFrame(columns=['Time', 'Ampl'])
    peaks, _ = find_peaks(df['Ampl'], prominence=(None, 0.6), distance=10)
    np.diff(peaks)
    ns["Time"] = df["Time"][peaks]
    ns["Ampl"] = df["Ampl"][peaks]

    return ns


def Figure(df, sig_df, xmin, xmax, ymin, ymax, hxmin, hxmax, df_sel, name):
    fig, ax = plt.subplots(dpi=150)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    font = {'family': 'arial', 'color':  'black', 'weight': 'bold', 'size': 12}
    # plt.axvspan(0, 2.5, facecolor='purple', alpha=0.1)
    # plt.axvspan(2.5, 34.5, facecolor='b', alpha=0.1)
    # plt.axvspan(34.5, 45, facecolor='r', alpha=0.1)
    plt.hlines(y=-10, xmin=hxmin, xmax=hxmax, linewidth=4, color='green')
    if (df_sel == 1):
        plt.plot(df["Time"], df["Ampl"], c="grey", lw=0.1)
    plt.plot([0, 1250000], [0, 0], 'k:')
    plt.plot(sig_df["Time"], sig_df["Ampl"], c="red")

    plt.axis([xmin, xmax, ymin, ymax])
    plt.xlabel("Time (s)", fontdict=font, labelpad=6)
    plt.ylabel("Photocurrent (nA)", fontdict=font, labelpad=10)
    plt.title(name, fontsize=15, fontweight="bold", y=1, pad=10)
    plt.show()
