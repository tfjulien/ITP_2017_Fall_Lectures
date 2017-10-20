#!/Users/bin/env/Python

"""
    @Author: Samson Jacob
    Purpose: Clean a MaxQuant File and get Barplots of missing values;not ultra recursive

    """

import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt


#files to analyze
Original = './Original.txt' #
LabVersion = './Lab2.txt'

#Functions
def get_columns(fil):
    """Get the columns from a file"""
    df=pd.read_table(fil,sep='\t',nrows=1,header=0)
    return df.columns.tolist()

def get_subset(df,str1='normalized_'):
    """return a subset of columns if columname is in string"""
    out = [col for col in df.columns if str1 in col]
    return df[out]

def rem_spaces(df1):
    """
    :param df1: a pandas dataframe
    :returns column names of original dataframe with spaces removed:
    note that the input dataframe itself is mutated
    """
    cols = df1.columns.tolist() # get the columns as a list
    cor = [] # initiate an empty corrected list
    for v in cols:
        cor.append(v.replace(' ', '_')) # replace space with underscore (str method)
    df1.columns = cor # replace
    return df1

def sum_missing(df1,filnam):
    """ sum the missing values in a row and saves a barplot"""
    df1['missing']= df1.isnull().sum(axis=1)
    f = pd.DataFrame(df1.missing.value_counts())
    fig,ax = plt.subplots() # initialize plotting
    ind = np.arange(len(f.index.tolist())) # get a range based on the index to set x-indices
    rects= ax.bar(ind,f.missing.tolist(),color='r') # plot the values with the indices
    ax.set_xticks(ind) # set the x values
    ax.set_xticklabels(f.index.tolist()) # set the xticks to the names of the missing vals
    plt.savefig(filnam) # save the figure
    return df1 
    
def format_df(df):
    """filter dataframe to remove contaminants/reverse and filter for unique proteins = 1"""
    ou=df[(df['Reverse']!='+') & (df['Contaminant']!='+')] # multiple boolean selection
    ou2= ou[ou.loc[:,'Number_of_proteins']==1] # loc selection
    return ou2

def main(file,write=True):
    """
    Input: A MaxQuant File
    Output: A cleaned dataframe, that also generates Barplots of the missing values
     """
    filenam = '/'+str(file)[:-4]+'.pdf' # for the saving of the barplot
    outflnam = '/'+str(file)[:-4]+'CLEANED'+'.txt'
    df= rem_spaces(pd.read_table(file,sep='\t',index_col=0))
    outdf = format_df(df)
    sub= get_subset(outdf,'normalized_') # get the normalized ratios
    m = sum_missing(sub,filenam)
    m2 =m[m.loc[:,'missing']==0]
    if write != True:
        return m2
    else:
        m2.to_csv(outflnam,sep='\t',na_rep=np.nan)

def merged_df(fil1,fil2):
    """ Takes 2 files and finds overlap and generates a boxplot"""
    df1 = main(fil1,False)
    df2 = main(fil2,False)
    mergeout= pd.merge(df1,df2,right_index=True,left_index=True) # merge
    dfmer =get_subset(mergeout) # delete the missing columns
    logtr = np.log2(dfmer)
    fig, ax = plt.subplots(figsize=(1,  1))
    logtr.plot(kind='box',legend=False,xticks=[])
    plt.savefig('h_boxplots.pdf')





