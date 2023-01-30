import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
noFilename = '[\/:*?"<>|]'
def file_re_name(title):
    for no in noFilename:
        title = title.replace(no,'')
    return title
def plot_index_scatter(data,responseName):
    x_values = list(range(0,len(data)))
    #print(x_values.shape())
    plt.scatter(x_values,data)
    plt.title(responseName)
    plt.savefig(file_re_name(responseName))
    plt.show()
def plot_index_compare_plot(data,responseName):
    plt.subplot(1,2,1)
    sns.distplot(data)
    plt.subplot(1,2,2)
    sns.boxplot(data)
    plt.savefig(file_re_name(responseName))
    plt.show()
def plot_IQR(data,responseName):
    if type(data) is np.ndarray:
        data=pd.DataFrame(data)
    elif type(data) is pd.DataFrame:
        pass
    percentile25 = data.quantile(0.25)
    percentile75 = data.quantile(0.75)
    iqr = percentile75 - percentile25
    upper_limit = percentile75 + 1.5 * iqr
    lower_limit = percentile25 - 1.5 * iqr
    new_data = data[(data.loc[:,0]<upper_limit.iloc[0]) & (data.loc[:,0]>lower_limit.iloc[0])]
    print(f"IQR 적용 전 shape : {data.shape} --> IQR 적용 후 shape : {new_data.shape}")
    fig, ax = plt.subplots(2,2,figsize=(16,10))
    sns.distplot(data.values,ax=ax[0,0])
    sns.boxplot(data.values,ax=ax[0,1])
    sns.distplot(new_data.values,ax=ax[1,0])
    sns.boxplot(new_data.values,ax=ax[1,1])
    ax[0,0].set_title("dist plot")
    ax[0,1].set_title("box plot")
    ax[1,0].set_title("dist plot (IQR filter)")
    ax[1,1].set_title("box plot (IQR filter)")
    plt.savefig(file_re_name(responseName))
    plt.show()
