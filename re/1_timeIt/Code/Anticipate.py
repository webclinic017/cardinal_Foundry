import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('df_main.csv')
data.isna().any(axis=1)