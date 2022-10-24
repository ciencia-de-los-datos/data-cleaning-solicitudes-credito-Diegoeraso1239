"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

import re
def format_date(str_date):
    d = re.search(r'(^\d+)\/(\d+)\/(\d+)', str_date, re.IGNORECASE)
    day = d.group(1)
    month = d.group(2)
    year = d.group(3)
    if len(day)>2:
        date = year + '/' + month + '/' + day
        return date
    else:
        date = day + '/' + month + '/' + year
        return date

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df= df[df.columns[1:]]
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    for i in df.columns:
        try:
            df[i] = df[i].str.lower()
        except:
            pass
    df.idea_negocio = df.idea_negocio.map(lambda x: re.sub(r'_|-', ' ', str(x)))
    df.barrio = df.barrio.map(lambda x: re.sub(r'-| ', '_', str(x)))
    # df.barrio = df.barrio.map(lambda x: re.sub(r'\s', '_', str(x)))
    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(format_date)
    df.monto_del_credito = df.monto_del_credito.map(lambda x: re.sub(r'\$', '', str(x)))
    df.monto_del_credito = df.monto_del_credito.map(lambda x: float(x.replace(',', '')))
    df['línea_credito'] = df['línea_credito'].map(lambda x: re.sub(r'_|-', ' ', str(x)))
    for i in df.columns:
            try:
                df[i] = df[i].str.strip()
            except:
                pass
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df
