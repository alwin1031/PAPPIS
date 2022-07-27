import pandas as pd
import numpy as np
import os


def Baseline(df, amp, avg):
    shf = sum(df['Ampl'][0:avg]) / avg
    df['Ampl'] = [amp * (x - shf) for x in df['Ampl']]

    return df


def Findpeak(df, hh, dis):
    from scipy.signal import find_peaks
    peaks, _ = find_peaks(df['Ampl'], height=hh, distance=dis)
    np.diff(peaks)

    fpk_df = pd.DataFrame(columns=['Time', 'Ampl'])
    fpk_df['Time'] = df['Time'][peaks]
    fpk_df['Ampl'] = df['Ampl'][peaks]

    return fpk_df


def Savgol_filter(df, w_size, p_order):
    from scipy.signal import savgol_filter
    df["Ampl"] = savgol_filter(df["Ampl"], w_size, p_order)
    return df


def Mean(df, min, max):
    sel = []
    df.reset_index(drop=True, inplace=True)
    for i in range(len(df)):
        if (min <= df['Time'][i] <= max):
            sel.append(df['Ampl'][i])
    area = sum(sel)
    mean = area/len(sel)
    print("{}s to {}s: {} nA".format(min, max, round(mean, 3)))

    return round(mean, 3)
