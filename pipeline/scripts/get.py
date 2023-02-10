# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# Add description here
#
# *Note:* You can open this file as a notebook (JupyterLab: right-click on it in the side bar -> Open With -> Notebook)


# %%
# Uncomment the next two lines to enable auto reloading for imported modules
# # %load_ext autoreload
# # %autoreload 2
# For more info, see:
# https://docs.ploomber.io/en/latest/user-guide/faq_index.html#auto-reloading-code-in-jupyter

# %% tags=["parameters"]
# If this task has dependencies, list them them here
# (e.g. upstream = ['some_task']), otherwise leave as None.
upstream = None

# This is a placeholder, leave it as None
product = None


# %%
import os
import pandas as pd
import numpy as np 
import nvdlib

# %%

results = nvdlib.searchCVE(pubStartDate = '2023-01-01 00:00', pubEndDate = '2023-02-07 00:00', key='9b21e27a-48f4-4581-9396-a1e17f8539c4  ', delay=6)

data = []
for eachCVE in results:
    data.append([eachCVE.id, eachCVE.score])
    
results = nvdlib.searchCVE(pubStartDate = '2023-01-01 00:00', pubEndDate = '2023-02-07 00:00', key='9b21e27a-48f4-4581-9396-a1e17f8539c4  ', delay=6)

data = []
for eachCVE in results:
    data.append([eachCVE.id, eachCVE.score])
    
    
df = pd.DataFrame(data, columns=["id", "score"])

df.drop(df.filter(regex='None').columns, axis=1, inplace=True)

df.to_csv('cve2_data.csv')

# %%
df = pd.read_csv('cve_data.csv')

# %%
df.head()


# %%
def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('None', '').replace(',', ''))
    return(x)

df['version'] = df['version'].apply(clean_currency)


# %%
def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('[', '').replace(',', ''))
    return(x)

df['version'] = df['version'].apply(clean_currency)

# %%
df.head(40)

# %%
