import pandas as pd
import os
import sys
from cmpc import Baseline, Findpeak, Savgol_filter, Mean

input_path = sys.argv[1]

# specifying an empty list for content
df_list = []

t_on, t_off, t_space, fpk_space = 0, 40, 5, 1300
# A shorter time span version
# t_on, t_off, t_space, fpk_space = 0, 16, 2, 3500

cep = int((t_off - t_on) / t_space)

for file in sorted(os.listdir(input_path)):
    print(file)

    if file.endswith('.csv'):
        # reading content into data frame
        df = pd.read_csv(input_path+'/'+file, skiprows=4)
        df = Baseline(df, 500, 1000)
        fpk_df = Findpeak(df, 0, fpk_space)
        fpk_df = Savgol_filter(fpk_df, 7, 2)
        mean_list = []
        for x in range(0, cep):
            temp = Mean(fpk_df, t_on + t_space * x, t_on + t_space*(x+1))
            mean_list.append(temp)
        df_list.append(mean_list)
        file_0 = os.path.splitext(file)[0]
        print('Done! d(//-v-)b')

print(df_list)
# Export to Excel file
df_list2 = pd.DataFrame(df_list)
df_list2.to_excel(input_path+'.xlsx', index=False, header=False)
