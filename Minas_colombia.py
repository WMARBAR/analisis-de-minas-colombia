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

#ARREGLO DE FECHAS
df_minas['Fecha del evento'] = pd.to_datetime(df_minas['Fecha del evento'] )
df_minas['Year'] = df_minas['Fecha del evento'].dt.year

#TOTALIZACION DE DATOS POR AÑOS:
df_pivot_YEAR=df_minas.pivot_table(index= 'Year',values=['Conteo_Eventos','#ACCIDENTES','#INCIDENTES'],aggfunc='sum')
df_pivot_YEAR["P_Accidentes"] = df_pivot_YEAR['#ACCIDENTES']/df_pivot_YEAR['Conteo_Eventos'] 
df_pivot_YEAR["P_Incidentes"] = df_pivot_YEAR['#INCIDENTES']/df_pivot_YEAR['Conteo_Eventos'] 
df_pivot_YEAR=df_pivot_YEAR.reset_index()

#TOTALIZACION DE DATOS POR FECHAS:
df_pivot_DATES=df_minas.pivot_table(index= 'Fecha del evento',values=['Conteo_Eventos','#ACCIDENTES','#INCIDENTES'],aggfunc='sum')
df_pivot_DATES["P_Accidentes"] = df_pivot_DATES['#ACCIDENTES']/df_pivot_DATES['Conteo_Eventos'] 
df_pivot_DATES["P_Incidentes"] = df_pivot_DATES['#INCIDENTES']/df_pivot_DATES['Conteo_Eventos'] 
df_pivot_DATES=df_pivot_DATES.reset_index()


