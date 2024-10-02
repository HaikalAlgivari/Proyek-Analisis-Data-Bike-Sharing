# Preparing Library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
import streamlit as st

# Load data
df_day = pd.read_csv('day.csv')
df_hour = pd.read_csv('hour.csv')

# Convert the 'dteday' column to datetime format
df_day['dteday'] = pd.to_datetime(df_day['dteday'])
df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])

# Drop the 'instant' column
df_day.drop('instant', axis=1, inplace=True)
df_hour.drop('instant', axis=1, inplace=True)

# Function to create the boxplot for mnth and cnt
def create_boxplot_mnth(df, title):
  plt.figure(figsize=(10, 6))
  sns.boxplot(x='mnth', y='cnt', data=df)
  plt.title(title)
  plt.xlabel('Bulan')
  plt.ylabel('Jumlah Penyewaan Sepeda')
  return plt

# Function to create the boxplot for hr and cnt
def create_boxplot_hr(df, title):
  plt.figure(figsize=(10, 6))
  sns.boxplot(x='hr', y='cnt', data=df)
  plt.title(title)
  plt.xlabel('Jam')
  plt.ylabel('Jumlah Penyewaan Sepeda')
  return plt

# Function to create the boxplot for season and cnt
def create_boxplot_season(df, title):
  plt.figure(figsize=(10, 6))
  sns.boxplot(x='season', y='cnt', data=df)
  plt.title(title)
  plt.xlabel('Musim')
  plt.ylabel('Jumlah Penyewaan Sepeda')
  return plt

# Function to create the boxplot for yr and cnt
def create_boxplot_yr(df, title):
  plt.figure(figsize=(10, 6))
  sns.boxplot(x='yr', y='cnt', data=df, hue='yr')
  plt.title(title)
  plt.xlabel('Tahun')
  plt.ylabel('Jumlah Penyewaan Sepeda')
  return plt


# Function to create the lineplot for dteday and cnt
def create_lineplot_dteday(df, title):
    plt.figure(figsize=(15, 6))
    sns.lineplot(x='dteday', y='cnt', data=df)
    plt.title(title)
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.xticks(rotation=45)
    return plt

def create_lineplot_mnth(df, title):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='mnth', y='cnt', data=df)
    plt.title(title)
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    return plt

# Function to create the heatmap for correlation
def create_heatmap_correlation(df, title):
    correlation_matrix = df.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(title)
    return plt

# Function to create the time series decomposition plot
def create_time_series_decomposition(df, title):
    df_daily = df.groupby('dteday')['cnt'].sum()
    decomposition = seasonal_decompose(df_daily, model='additive', period=30)
    plt.rcParams['figure.figsize'] = (25, 10)
    decomposition.plot()
    return plt


# Streamlit dashboard
st.title('Bike Sharing Data Analysis Dashboard')

# Sidebar navigation
st.sidebar.title('Navigation')
selected_tab = st.sidebar.radio('Select Tab', ['Visualisasi & Analisis Deskriptif', 'Analisis Lanjutan'])


# Visualisasi & Analisis Deskriptif
if selected_tab == 'Visualisasi & Analisis Deskriptif':
    st.header('Visualisasi & Analisis Deskriptif')

    st.subheader('Distribusi Jumlah Penyewaan Sepeda terhadap Waktu')
    st.pyplot(create_lineplot_dteday(df_day, 'Distribusi Jumlah Penyewaan Sepeda per Hari terhadap Waktu'))
    st.pyplot(create_lineplot_dteday(df_hour, 'Distribusi Jumlah Penyewaan Sepeda per Jam terhadap Waktu'))

    st.subheader('Distribusi Jumlah Penyewaan Sepeda Berdasarkan Musim')
    st.pyplot(create_boxplot_season(df_day, 'Distribusi Jumlah Penyewaan Sepeda per Hari Berdasarkan Musim'))
    st.pyplot(create_boxplot_season(df_hour, 'Distribusi Jumlah Penyewaan Sepeda per Jam Berdasarkan Musim'))

    st.subheader('Perbedaan Jumlah Penyewaan Sepeda Antara Tahun 2011 dan 2012')
    st.pyplot(create_boxplot_yr(df_day, 'Distribusi Jumlah Penyewaan Sepeda per Hari Berdasarkan Tahun'))
    st.pyplot(create_boxplot_yr(df_hour, 'Distribusi Jumlah Penyewaan Sepeda per Jam Berdasarkan Tahun'))

    st.subheader('Jumlah Penyewaan Sepeda Berdasarkan Bulan')
    st.pyplot(create_lineplot_mnth(df_day, 'Distribusi Jumlah Penyewaan Sepeda per Hari terhadap Bulan'))
    st.pyplot(create_lineplot_mnth(df_hour, 'Distribusi Jumlah Penyewaan Sepeda per Jam terhadap Bulan'))

    st.subheader('Jumlah Penyewaan Sepeda Berdasarkan Jam')
    st.pyplot(create_boxplot_hr(df_hour, 'Distribusi Jumlah Penyewaan Sepeda terhadap Jam'))

# Analisis Lanjutan
elif selected_tab == 'Analisis Lanjutan':
    st.header('Analisis Lanjutan')

    st.subheader('Analisis Korelasi')
    st.pyplot(create_heatmap_correlation(df_hour, 'Correlation Matrix of df_hour'))
    st.pyplot(create_heatmap_correlation(df_day, 'Correlation Matrix of df_day'))

    st.subheader('Time Series Decomposition')
    st.pyplot(create_time_series_decomposition(df_day, 'Time Series Decomposition of df_day'))
    st.pyplot(create_time_series_decomposition(df_hour, 'Time Series Decomposition of df_hour'))
