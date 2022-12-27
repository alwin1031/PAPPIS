# PAPPIS
CMPC (Continuous Measurement of Photocurrent) is a biomolecular level resistence change measuring technique based on the LV-ITO device. Those who have performed CMPC experiments must continue to perform data processing to receive comparable results. The data processing method is described below.

## Quick Startup
1. Go to Code button, download .zip file.
2. Download **Python** from the official website: https://www.python.org/downloads
3. For Mac users, open Terminal. For Windows users, open PowerShell.
4. Run `pip3 install pandas`, `pip3 install scipy` and `pip3 install openpyxl`.
5. Create a new working directory. Remember it!
6. Move the entire code to your current working directory.
6. Open terminal on that directory and you are ready to process your data! (Go to **Data Processing** session)

## For expert users
1. I'm glad that you challenge yourself as being an expert user! Expert doesn't mean it is hard, but powerful!
2. Download **Python** from the official website: https://www.python.org/downloads
2. Download **Git** from the official website: https://git-scm.com/downloads
3. Open Terminal or PowerShell.
4. Run `pip3 install pandas`, `pip3 install scipy` and `pip3 install openpyxl`.
5. Type in `pwd` in the command line to check your current working directory. Remember it!
6. To change your current working directory, use `cd another_location`. It would be helpful to run `ls` to find out what you have under this working directory.
7. Run <code>git clone https://github.com/alwin1031/PAPPIS.git</code>. The processing file will be downloaded in your current working directory.
8. You can always restore the code by repeating Step 6 in your working directory.

Note: If you are interested in this program and want to contributed to our project, we highly recommend you to download git and forge this version under your own account.


## Data Processing

### Path relationship
<pre> 
User
| -- Working directory (Terminal here)
     |
     | -- PAPPIS
     |    | -- Python file
     |
     | -- Data directory
     |    | -- your data here
     |
     | -- Excel output file
</pre>


1. Open Terminal or PowerShell, and `cd` to your working directory, e.g., **work_001**.
2. Prepare your CMPC data, e.g., **data_001.csv** in your working directory **work_001**.
3. Run `python PAPPIS/run.py work_001`.
4. DONE! You will receive an Excel file with time-averaging data.


## Adjustable Parameters
You can use any IDE (Integrated Development Environment) or simply the Notebook (記事本) to edit the Python file. Here, we recommend VScode: https://code.visualstudio.com.

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
