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
upstream = ['get']

# This is a placeholder, leave it as None
product = None


# %%
import pandas as pd

# %%
df = pd.read_csv(upstream['get']['data'])


# %%
#Cleaning Version Col
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
#Cleaning Score Col
def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('None', '').replace(',', ''))
    return(x)

df['score'] = df['score'].apply(clean_currency)


# %%
def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('[', '').replace(',', ''))
    return(x)

df['score'] = df['score'].apply(clean_currency)


# %%
#Cleaning severity Col
def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('None', '').replace(',', ''))
    return(x)

df['severity'] = df['severity'].apply(clean_currency)


# %%
def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('[', '').replace(',', ''))
    return(x)

df['severity'] = df['severity'].apply(clean_currency)

# %%
df.dropna

# %%
df.head(70)

# %%

# %%
