import pandas as pd;    import numpy as np;     import matplotlib.pyplot as plt

# read csv into 4 DataFrame: BCG, Campak, DPT, Polio

BCG = pd.read_csv('Balita Terimunisasi BCG 1995-2017.csv', na_values='n.a')
# BCG.info()
Campak = pd.read_csv('Balita Terimunisasi Campak 1995-2017.csv', na_values='n.a')
# Campak.info()
DPT = pd.read_csv('Balita Terimunisasi DPT 1995-2017.csv', na_values='n.a')
# DPT.info()
Polio = pd.read_csv('Balita Terimunisasi Polio 1995-2017.csv', na_values='n.a')
# Polio.info()

# Cleaning data: Interpolate
# print(type(BCG.iloc[4, 1])) #<class 'numpy.float64'>
BCG = BCG.interpolate('linear', Axis = 0)      # print(BCG)
Campak = Campak.interpolate('linear', Axis = 0)
DPT = DPT.interpolate('linear', Axis = 0)
Polio = Polio.interpolate('linear', Axis = 0)

BCG.columns = ['Tahun', 'Persen']
Campak.columns = ['Tahun', 'Persen']
DPT.columns = ['Tahun', 'Persen']
Polio.columns = ['Tahun', 'Persen']

# Create Graphs
plt.figure('Figure 1: Persentasi balita terimunisasi 1995-2017', figsize=(13,8))
# plt.subplot(row,col,position)
plt.subplot(2,2,1)
plt.bar(BCG.Tahun, BCG.Persen, color='red')
plt.title('BCG')
plt.xticks(BCG['Tahun'],np.arange(1995,2018),rotation = 90)

plt.subplot(2,2,2)
plt.bar(Campak.Tahun, Campak.Persen, color='g')
plt.title('Campak')
plt.xticks(Campak['Tahun'],np.arange(1995,2018),rotation = 90)

plt.subplot(2,2,3)
plt.bar(DPT.Tahun, DPT.Persen, color='y')
plt.title('DPT')
plt.xticks(DPT['Tahun'],np.arange(1995,2018),rotation = 90)

plt.subplot(2,2,4)
plt.bar(Polio.Tahun, Polio.Persen, color='b')
plt.title('Polio')
plt.xticks(Polio['Tahun'],np.arange(1995,2018),rotation = 90)

plt.show()
plt.clf()

BCG.Persen2 = (100 - BCG.Persen)
Campak.Persen2 = (100 - BCG.Persen)
DPT.Persen2 = (100 - BCG.Persen)
Polio.Persen2 = (100 - BCG.Persen)
# print(BCG.Persen2)

plt.figure('Figure 2: Persentasi balita tak terimunisasi 1995-2017', figsize=(13,8))
# plt.subplot(row,col,position)
plt.subplot(2,2,1)
plt.bar(BCG.Tahun, BCG.Persen2, color='r')
plt.title('BCG')
plt.xticks(BCG['Tahun'],np.arange(1995,2018),rotation = 90)

plt.subplot(2,2,2)
plt.bar(Campak.Tahun, BCG.Persen2, color='g')
plt.title('Campak')
plt.xticks(Campak['Tahun'],np.arange(1995,2018),rotation = 90)

plt.subplot(2,2,3)
plt.bar(DPT.Tahun, BCG.Persen2, color='y')
plt.title('DPT')
plt.xticks(DPT['Tahun'],np.arange(1995,2018),rotation = 90)

plt.subplot(2,2,4)
plt.bar(Polio.Tahun, BCG.Persen2, color='b')
plt.title('Polio')
plt.xticks(Polio['Tahun'],np.arange(1995,2018),rotation = 90)

plt.show()
plt.clf()