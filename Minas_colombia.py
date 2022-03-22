import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

#Agregar base de datos de minas del gobierno de colombia
df_minas = pd.read_excel("D:/WILSON MARTINEZ/programas/python/Analisis_Minas/Base_minas_colombia_analisis.xlsx",sheet_name="Evento_minas_RAW")
#Arreglo de caracteres con espacio el la columna "presunto actor responsable"
df_minas['Presunto actor responsable']=df_minas['Presunto actor responsable'].str.strip(' ')

#Creacion de las funciones de incidentes y accidentes: 
#FUNCION DE ACCIDENTE
def get_Accidentes(var1):
    if var1 == 'Accidente':
        return 1
    else:
        return 0

#FUNCION DE INCIDENTE
def get_Incidentes(var1):
    if var1 == 'Incidente':
        return 1
    else:
        return 0

#ARREGLOS BINARIOS
df_minas['Conteo_Eventos']=1
df_minas['#ACCIDENTES'] = df_minas['Eventos'].apply(lambda x: get_Accidentes(x))
df_minas['#INCIDENTES'] = df_minas['Eventos'].apply(lambda x: get_Incidentes(x))