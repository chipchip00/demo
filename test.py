import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('monthly.csv')
df1 = df[df['Date'].str.contains("1950")]
print(df1)