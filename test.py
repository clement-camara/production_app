import streamlit as st
import psycopg2
from psycopg2 import OperationalError
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
from config import name, user, password, host, port



#engine = create_engine(f'postgresql://{user}:{password}@{host}/{name}')
#ngine
def create_connection(db_name,db_user,db_password,db_host,db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port,
        )
        cursor = connection.cursor()
        print("YaY")
    except OperationalError as error:
        print(f"Nope '{error}'")
    return connection


def sql_request_to_db(request = str):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(request)
            result = cursor.fetchall()
    return result

connection = create_connection(name, user, password, host, port)




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


countries = sql_request_to_db(request)

df_import = pd.read_sql(request, connection)
df_import
