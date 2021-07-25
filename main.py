import tkinter as tk
from tkinter import StringVar, filedialog
from tkinter import ttk
import os
from tkinter.constants import DISABLED, NORMAL
import pandas as pd
from photocurrent import Baseline, Correction, Findpeak, Mean, Figure

window = tk.Tk()
window.title('Photocurrent Genie')
window.geometry('300x700')

"""
class section:

    def __init__(self, frame):
        frame = tk.Frame(window)
        frame.pack()
        self.frame = frame

    def entry_func(self, txt, wit, denum):
        self.label = tk.Label(self.frame, text = txt)
        self.label.pack(side = tk.LEFT)
        self.entry = tk.Entry(self.frame, width = wit)
        self.entry.insert(0, denum)
        self.entry.pack(side = tk.LEFT)
"""

def input(s, ss, txt, wit, denum):
    frame = str('frame_'+ss)
    label = str('label_'+s)
    entry = str(s+'_entry')
    if (s == ss):
        globals()[frame] = tk.Frame(window)
        globals()[frame].pack(side=tk.TOP)
    globals()[label] = tk.Label(globals()[frame], text=txt)
    globals()[label].pack(side=tk.LEFT)
    globals()[entry] = tk.Entry(globals()[frame], width=wit)
    globals()[entry].insert(0, denum)
    globals()[entry].pack(side=tk.LEFT)


def disable(t, s):
    cat = str('chk_'+t+'_value')
    entry = str(s+'_entry')
    if (globals()[cat].get() != 1):
        globals()[entry].config(state=DISABLED)
    else:
        globals()[entry].config(state=NORMAL)


def sep():
    ttk.Separator(window, orient='horizontal').pack(fill='x')


class run:
    def __init__(self):
        pass

    def browsefunc(self):
        file_path = filedialog.askopenfilenames(filetypes=[('CSV', '*.csv',)])
        for f in file_path:
            input_path = f.split('.')[0]+'.csv'

        self.input_path = input_path
        path.configure(text=input_path)
        return input_path

    def Genie(self):
        input_path = self.input_path

        df = pd.read_csv(input_path, skiprows=4)
        input_path = os.path.splitext(input_path)[0]

        # Baseline
        if (chk_baseline.get() == 1):
            ampr = int(ampr_entry.get())
            avgnum = int(avgnum_entry.get())
            df = Baseline(df, ampr, avgnum)
        else:
            pass

        # Correction
        if (chk_correction.get() == 1):
            cb = float(cb_entry.get())
            ca = float(ca_entry.get())
            cor_df = Correction(df, cb, ca)
        else:
            cor_df = df

        # Findpeak
        if (chk_findpeak.get() == 1):
            hh = float(hh_entry.get())
            dis = float(dis_entry.get())
            fpk_df = Findpeak(cor_df, hh, dis)
        else:
            fpk_df = cor_df
            hh_entry.config(state=DISABLED)

        # Post-Baseline
        if (chk_pbaseline.get() == 1):
            avgnum2 = int(avgnum2_entry.get())
            sig_df = Baseline(fpk_df, 1, avgnum2)
        else:
            sig_df = fpk_df

        mean_r = Mean(sig_df, float(calmin_entry.get()),
                      float(calmax_entry.get()))
        meanp = 'Average：{}, from area {}'.format(mean_r[1], mean_r[0])
        mean.configure(text=meanp)

        # Figure
        a = [chk_fig_value.get(), chk_dfshow_value.get()]
        name = str(name_entry.get())
        xmin, xmax, ymin, ymax, hxmin, hxmax = int(xmin_entry.get()), int(
            xmax_entry.get()), int(ymin_entry.get()), int(ymax_entry.get()), int(hxmin_entry.get()), int(hxmax_entry.get())
        if (a == [1,1]):
            Figure(df, sig_df, xmin, xmax, ymin, ymax, hxmin, hxmax, 1, name)
        elif(a == [1,0]):
            Figure(df, sig_df, xmin, xmax, ymin, ymax, hxmin, hxmax, 0, name)
        elif(a == [0,1] or a == [0,0]):
            pass


data = run()
# ---- Data Import
label_import = tk.Label(window, text='Data Import', bd=5)   # Import label
label_import.pack(side=tk.TOP)
frame_import = tk.Frame(window)  # Import frame /start
frame_import.pack(side=tk.TOP)
button_browse = tk.Button(frame_import, text="Browse",
                          command=data.browsefunc)   # Browse button
button_browse.pack(side=tk.TOP)
path = tk.Label(frame_import, wraplength=0)  # Browse path display
path.pack(side=tk.TOP)
sep()

# ---- Baseline label
chk_baseline = tk.BooleanVar()
chk_baseline.set(True)
chk_baseline_btn = tk.Checkbutton(
    window, text='Baseline', var=chk_baseline, bd=5, command=lambda: (disable('baseline', 'ampr'), disable('baseline', 'avgnum')))
chk_baseline_btn.pack(side=tk.TOP)

input('ampr', 'ampr', 'Ampl factor (nA/V)', 10, '500')  # Ampr frame
input('avgnum', 'avgnum', 'Average number (counts)', 10, '1000')  # Avgnum frame
sep()

# ---- Correction label
chk_correction = tk.BooleanVar()
chk_correction.set(True)
chk_correction_btn = tk.Checkbutton(
    window, text='Correction', var=chk_correction, bd=5, command=lambda: (disable('correction', 'cb'), disable('correction', 'ca')))
chk_correction_btn.pack(side=tk.TOP)
input('cb', 'cb', 'cb (cb)', 10, '2')  # cb frame
input('ca', 'ca', 'ca (ca)', 10, '0.02')  # ca frame
sep()

# ---- Findpeak label
chk_findpeak = tk.BooleanVar()
chk_findpeak.set(True)
chk_findpeak_btn = tk.Checkbutton(
    window, text='Findpeak', var=chk_findpeak, bd=5, command=lambda: (disable('findpeak', 'hh'), disable('findpeak', 'dis')))
chk_findpeak_btn.pack(side=tk.TOP)
input('hh', 'hh', 'height (nA)', 10, '0')  # hh frame
input('dis', 'dis', 'distance (data)', 10, '1500')  # dis frame
sep()

# ---- Post-Baseline label
chk_pbaseline = tk.BooleanVar()
chk_pbaseline.set(True)
chk_pbaseline_btn = tk.Checkbutton(
    window, text='Post-Baseline', var=chk_pbaseline, bd=5, command=lambda: (disable('pbaseline', 'amfr2'), disable('pbaseline', 'avgnum2')))
chk_pbaseline_btn.pack(side=tk.TOP)
input('avgnum2', 'avgnum2', 'Average number (counts)', 10, '150')  # Avgnum2 frame
sep()

# ---- Figure label
chk_fig_value = tk.BooleanVar()
chk_fig_value.set(True)
chk_fig = tk.Checkbutton(window, text='Figure', var=chk_fig_value, bd=5, command=lambda: (disable('fig',
                                                                                                  'name'), disable('fig', 'xmin'), disable('fig', 'xmax'), disable('fig', 'ymin'), disable('fig', 'ymax'), disable('fig', 'hxmin'), disable('fig', 'hxmax')))
chk_fig.pack(side=tk.TOP)
input('name', 'name', 'Title', 30, '')  # Name frame
input('xmin', 'xmin', 'xmin', 5, '0')  # Xmin frame
input('xmax', 'xmin', 'xmax', 5, '45')  # Xmin frame
input('ymin', 'ymin', 'ymin', 5, '-20')  # Ymin frame
input('ymax', 'ymin', 'ymax', 5, '20')  # Ymin frame
input('hxmin', 'hxmin', 'hxmin', 5, '10')  # Ymin frame
input('hxmax', 'hxmin', 'hxmax', 5, '35')  # Ymin frame

# ---- dfshow
chk_dfshow_value = tk.BooleanVar()
chk_dfshow_value.set(True)
chk_dfshow = tk.Checkbutton(window, text='Show original data',
                            var=chk_dfshow_value, bd=5)
chk_dfshow.pack(side=tk.TOP)

input('calmin', 'calmin', 'cal_min', 5, '15')  # Ymin frame
input('calmax', 'calmin', 'cal_max', 5, '30')  # Ymin frame

mean = tk.Label(window, wraplength=0)  # Browse path display
mean.pack(side=tk.TOP)

calculate_btn = tk.Button(window, text='Run', command=data.Genie)
calculate_btn.pack()


window.mainloop()
