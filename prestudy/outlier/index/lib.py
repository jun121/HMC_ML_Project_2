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
    outlier = data[(data.loc[:,0]>upper_limit.iloc[0]) | (data.loc[:,0]<lower_limit.iloc[0])]
    outlier.columns=[responseName]
    print(f"IQR 적용 전 shape : {data.shape} --> IQR 적용 후 shape : {new_data.shape}")
    print(f"{file_re_name(responseName)} outlier DoE nuber is {outlier.index}")
    fig, ax = plt.subplots(2,2,figsize=(16,10))
    sns.distplot(data.values,ax=ax[0,0])
    sns.boxplot(data.values,ax=ax[0,1])
    sns.distplot(new_data.values,ax=ax[1,0])
    sns.boxplot(new_data.values,ax=ax[1,1])
    ax[0,0].set_title("dist plot")
    ax[0,1].set_title("box plot")
    ax[1,0].set_title("dist plot (IQR filter)")
    ax[1,1].set_title("box plot (IQR filter)")
    plt.savefig("IQR_"+file_re_name(responseName))
    outlier.to_csv("IQR_"+file_re_name(responseName)+".csv",sep=",")
    plt.show()
def plot_z_score(data,responseName,sigma=3):
    # sigma default value is 3

    if type(data) is np.ndarray:
        data=pd.DataFrame(data)
    upper_limit = data.mean()+sigma*data.std()
    lower_limit = data.mean()-sigma*data.std()
    new_data = data[(data.loc[:,0]<upper_limit.iloc[0]) & (data.loc[:,0]>lower_limit.iloc[0])]
    outlier = data[(data.loc[:,0]>upper_limit.iloc[0]) | (data.loc[:,0]<lower_limit.iloc[0])]
    outlier.columns=[responseName]
    print(f"z score 적용 전 shape : {data.shape} --> z score 적용 후 shape : {new_data.shape}")
    print(f"{file_re_name(responseName)} outlier DoE nuber is {outlier.index}")
    fig, ax = plt.subplots(2,2,figsize=(16,10))
    sns.distplot(data.values,ax=ax[0,0])
    sns.boxplot(data.values,ax=ax[0,1])
    sns.distplot(new_data.values,ax=ax[1,0])
    sns.boxplot(new_data.values,ax=ax[1,1])
    ax[0,0].set_title("dist plot")
    ax[0,1].set_title("box plot")
    ax[1,0].set_title("dist plot (z score filter)")
    ax[1,1].set_title("box plot (z score filter)")
    plt.savefig("z_score_"+file_re_name(responseName))
    outlier.to_csv("z_score"+file_re_name(responseName)+".csv",sep=",")
    plt.show()