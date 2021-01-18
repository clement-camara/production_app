
import streamlit as st
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
from config import name, user, password, host, port



engine = create_engine(f'postgresql://{user}:{password}@{host}/{name}')
engine



request = """
    SELECT year AS years, value AS values , countries.name AS countries, flows.name AS flows, products.name AS products
        FROM quantities
            JOIN countries
                ON quantities.country_id = countries.id
            JOIN flows
                ON quantities.flow_id = flows.id
            JOIN products
                ON products.id = quantities.product_id
            WHERE flows.name = 'Imports (ktoe)'
                AND countries.name = 'France'
                AND products.name = 'Renewables and waste'
                AND products.name <> 'Total'
                ;
"""


df_import = pd.read_sql(request, engine)

st.title('Visualisation  basé sur la France')

st.subheader('dataframe \n  1) importation des energies renouvelables en France')
st.write(df_import)
st.subheader('Importation des énergies renouvelables en France')
st.set_option('deprecation.showPyplotGlobalUse', False)

hist_values = sns.set_theme(style="white")
fig, ax = plt.subplots(figsize=(15, 10))
sns.lineplot(
ax = ax,
x="years",
y="values",
hue="products",
style="products",
data=df_import,
palette="deep")
ax.grid(True)
ax.annotate('Sommet de la terre', xy=(1992,800), xytext=(1993, 700),
            arrowprops=dict(facecolor='black', shrink=0.05),
            ).set_fontsize(15)
sns.regplot(ax = ax, x="years",y="values", data=df_import)
ax.annotate('protocole de Kyoto', xy=(1997,900), xytext=(1998, 900),
            arrowprops=dict(facecolor='black', shrink=0.05),
            ).set_fontsize(15)
ax.annotate('accord de Paris', xy=(2016,900), xytext=(2017, 900),
            arrowprops=dict(facecolor='black', shrink=0.05),
            ).set_fontsize(15)
ax.set_title("Evolution de l'importation des énergies renouvelables en France").set_fontsize(15)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=2)
plt.axvline(x = 1992, color='green')
plt.axvline(x = 1997, color='red')
plt.axvline(x = 2016, color='blue')
plt.ylim(0, 1000)
st.pyplot(hist_values)


print(" ")
print(" ")
print(" ")
print(" ")
print(" ")


st.subheader("Evolution des energies renouvelables en France par flux")

energies_renouvelable = """
    SELECT year AS years, value AS values , countries.name AS countries, flows.name AS flows, products.name AS products
        FROM quantities
            JOIN countries
                ON quantities.country_id = countries.id
            JOIN flows
                ON quantities.flow_id = flows.id
            JOIN products
                ON products.id = quantities.product_id
            WHERE (flows.name = 'Imports (ktoe)'
                OR flows.name = 'Total final consumption (ktoe)'
                OR flows.name = 'Production (ktoe)')
                AND countries.name = 'France'
                AND products.name = 'Renewables and waste'
                AND products.name <> 'Total'
                ;
"""

df_energies_renouvelable = pd.read_sql(energies_renouvelable, engine)
st.subheader('dataframe \n production / consommation / exportation / energies renouvelable')
df_energies_renouvelable


erergy_renouvelable_graph = sns.set_theme(style="white")
fig, ax = plt.subplots(figsize=(22, 13))
sns.lineplot(
ax = ax,
x="years",
y="values",
hue="products",
style="flows",
data=df_energies_renouvelable,
palette="deep")
ax.grid(True)
ax.annotate('Sommet de la terre', xy=(1992,30000), xytext=(1993, 29000),
            arrowprops=dict(facecolor='black', shrink=0.05),
            ).set_fontsize(20)
sns.regplot(ax = ax, x="years",y="values", data=df_energies_renouvelable)
ax.annotate('protocole de Kyoto', xy=(1997,37000), xytext=(1998, 36000),
            arrowprops=dict(facecolor='black', shrink=0.05),
            ).set_fontsize(20)
ax.annotate('accord de Paris', xy=(2016,37000), xytext=(2017, 36000),
            arrowprops=dict(facecolor='black', shrink=0.05),
            ).set_fontsize(20)
ax.set_title("evolution des energies par flux et par énergies dans le temps en France en (ktoe)").set_fontsize(20)
ax.legend(loc='center left', bbox_to_anchor=(0, 0.7), ncol=2, fontsize=15)
plt.axvline(x = 1992, color='green')
plt.axvline(x = 1997, color='red')
plt.axvline(x = 2016, color='blue')
ax.xaxis.label.set_size(20)
ax.yaxis.label.set_size(20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylim(0, 40000)
st.pyplot(erergy_renouvelable_graph)





print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

st.subheader("Evolution des energies en France par flux et types d'énergies")

energies = """
    SELECT year AS years, value AS values , countries.name AS countries, flows.name AS flows, products.name AS products
        FROM quantities
            JOIN countries
                ON quantities.country_id = countries.id
            JOIN flows
                ON quantities.flow_id = flows.id
            JOIN products
                ON products.id = quantities.product_id
            WHERE (flows.name = 'Imports (ktoe)'
                OR flows.name = 'Total final consumption (ktoe)'
                OR flows.name = 'Production (ktoe)')
                AND countries.name = 'France'
                AND (products.name = 'Oil products'
                OR products.name = 'Renewables and waste'
                OR products.name = 'Crude, NGL and feedstocks'
                OR products.name = 'Coal, peat and oil shale')
                AND products.name <> 'Total'
                ;
"""

df_energies = pd.read_sql(energies, engine)
st.subheader('dataframe \n production / consommation / exportation / energies fossile et renouvelable')
df_energies


erergy_graph = sns.set_theme(style="white")
fig, ax = plt.subplots(figsize=(22, 13))
sns.lineplot(
ax = ax,
x="years",
y="values",
hue="products",
style="flows",
data=df_energies,
palette="deep")
ax.grid(True)
ax.annotate('Sommet de la terre', xy=(1992,118000), xytext=(1993, 117000),
            arrowprops=dict(facecolor='black', shrink=0.05),
            ).set_fontsize(20)
#sns.regplot(ax = ax, x="years",y="values", data=df_energies)
ax.annotate('protocole de Kyoto', xy=(1997,131000), xytext=(1998, 130000),
            arrowprops=dict(facecolor='black', shrink=0.05),
            ).set_fontsize(20)
ax.annotate('accord de Paris', xy=(2016,131000), xytext=(2017, 130000),
            arrowprops=dict(facecolor='black', shrink=0.05),
            ).set_fontsize(20)
ax.set_title("evolution des energies par flux et par énergies dans le temps en France en (ktoe)").set_fontsize(20)
ax.legend(loc='center left', bbox_to_anchor=(0, 0.3), ncol=2, fontsize=15)
plt.axvline(x = 1992, color='green')
plt.axvline(x = 1997, color='red')
plt.axvline(x = 2016, color='blue')
ax.xaxis.label.set_size(20)
ax.yaxis.label.set_size(20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylim(0, 120000)
plt.ylim(0, 140000)
st.pyplot(erergy_graph)


