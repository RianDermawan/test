# to make it easier to read multiple excel files, every file name excel must be in order such as data1, data2, data3 etc.  Because we use loop algorithm
# example my directory folder is D:\\test, it folder have file such as laporan_iklim_harian (0), laporan_iklim_harian (1), ....  
import pandas as pd
path = 'D:\\test-lagi\\laporan_iklim_harian (' # file path
isi = [] # empyt list

try:
    # using loop for generate data to list 
    for i in range(12): # optional range, it depends on your data. My data have is 11 
        data_i = pd.read_excel(path+str(i)+').xlsx') # read every excel
        data_i = [data_i] # change type data to list
        isi = isi + data_i  # combine all data into a list
except:
    print('error')
    
# combine data into one file
data_baru = pd.concat(isi, axis=0)

# export excel 
data_baru.to_excel('D:\\test-lagi\\data_baru.xlsx', index=False)