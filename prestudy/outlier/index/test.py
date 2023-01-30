import os
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
from lib import *
os.chdir(os.path.dirname(__file__))
cwd = os.getcwd()

X_no = 54
root = Tk()
data_dir=filedialog.askdirectory(parent=root,initialdir=cwd,title='Please select a directory')
print(data_dir)
file_lst = os.listdir(data_dir)
data_name_lst = [f for f in file_lst if f.endswith(".csv")]
print(data_name_lst)
for idx,name in enumerate(data_name_lst):
    data = pd.read_csv(os.path.join(data_dir,name),delimiter=',')
    column_name = list(data.columns)
    x_column_name = column_name[0:X_no]
    Y_no =  len(data.columns)-X_no
    X = data.iloc[:,0:X_no].values
    Y = data.iloc[:,X_no:].values
    for j in range(np.size(Y,1)):
        ColName = name.split(".")[0] + '_' + column_name[X_no + j]
        #plot_index_scatter(Y[:,j],ColName)
        #plot_index_compare_plot(Y[:,j],ColName)
        plot_IQR(Y[:,j],ColName)