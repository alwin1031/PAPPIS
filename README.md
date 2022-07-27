# PAPPIS
CMPC (Continuous Measurement of Photocurrent) is a continous measurement of resistance change in the LV-ITO device employing photocurrent. Those who have performed CMPC experiments must proceed with further data processing to interpret the results.

## Install and Setup Prerequisites
1. Download **Python** from the official website: https://www.python.org/downloads/
2. Download **Git** from the official website: https://git-scm.com/downloads
3. For Mac users, open Terminal (終端機). For Windows users, open PowerShell.
4. Type in `pwd` in the command line to check your current working directory. Remember it!
5. To change your current working directory, use `cd another_location`. It would be helpful to run `ls` to find out what you have under this working directory.
6. Run <code>git clone https://github.com/alwin1031/PAPPIS.git</code>. The processing file will be downloaded in your current working directory.
7. You can always restore the code by repeating Step 6 in your working directory.


## Data Processing
1. Open Terminal or PowerShell, and `cd` to your working directory.
2. Prepare your CMPC data (e.g., data.csv) in *your_data_directory*.
3. Run `python PAPPIS/run.py your_data_directory/data.csv`.
4. That's it! You will receive an Excel file with time-averaging data.


## Parameters to be Adjusted
You can use any IDE (Integrated Development Environment) or simply Notebook (記事本) to edit the Python file. Here, we recommend VScode: https://code.visualstudio.com.

CMPC has 20-s and 50-s time span option. You can uncommand one of each as shown below to match the parameters in data processing.
> Time span: 50-s (Default)  
> <pre><code>t_on, t_off, t_space, fpk_space = 0, 40, 5, 1300
> #t_on, t_off, t_space, fpk_space = 0, 16, 2, 3500</pre></code>

> Time span: 20-s
> <pre><code>#t_on, t_off, t_space, fpk_space = 0, 40, 5, 1300
> t_on, t_off, t_space, fpk_space = 0, 16, 2, 3500</pre></code>

If not necessary, please do not modify the function file cmpc.py.

## Citation
Please cite as following:
```
Chen, Y.H. (2022). Python Program for Continuous Measurement of Photocurrent (Version 1.0.0) [Computer software]. https://github.com/alwin1031/PAPPIS
