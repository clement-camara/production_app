
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
df_import
