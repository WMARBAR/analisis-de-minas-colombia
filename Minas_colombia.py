import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime as dt

#Agregar base de datos de minas del gobierno de colombia
df_minas = pd.read_excel("D:/WILSON MARTINEZ/programas/python/Analisis_Minas/Base_minas_colombia_analisis.xlsx",sheet_name="Evento_minas_RAW")

#Agregando la informacion del calendario
df_GLOBAL_CALENDAR = pd.read_excel("D:/WILSON MARTINEZ/programas/python/CALENDAR_GLOBAL.xlsx",sheet_name="Calendar")
df_GLOBAL_CALENDAR['date'] = pd.to_datetime(df_GLOBAL_CALENDAR['date'] )
df_GLOBAL_CALENDAR['date_g']=df_GLOBAL_CALENDAR['date'].dt.strftime("%d/%m/%Y")
df_minas.to_excel(r"D:/WILSON MARTINEZ/programas/Proyectos GIT/Proyecto_minas_python/Bases_de_datos/Full_Minas.xlsx",
                                          sheet_name='Minas_full', encoding = 'utf-8', index = True)

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
df_minas['date_g']=df_minas['Fecha del evento'].dt.strftime("%d/%m/%Y")
df_minas['Year'] = df_minas['Fecha del evento'].dt.year

#AÑADIENDO LAS COLUMNAS DEL CALENDARIO
df_minas=pd.merge(df_minas,df_GLOBAL_CALENDAR,on='date_g',how='left')
df_minas.to_excel(r"D:/WILSON MARTINEZ/programas/Proyectos GIT/Proyecto_minas_python/Bases_de_datos/Full_Minas.xlsx",
                                          sheet_name='Minas_full', encoding = 'utf-8', index = True)

#TOTALIZACION DE DATOS POR AÑOS:
df_minas_pivot_YEAR=df_minas.pivot_table(index= 'Year',values=['Conteo_Eventos','#ACCIDENTES','#INCIDENTES'],aggfunc='sum')
df_minas_pivot_YEAR["P_Accidentes"] = df_minas_pivot_YEAR['#ACCIDENTES']/df_minas_pivot_YEAR['Conteo_Eventos'] 
df_minas_pivot_YEAR["P_Incidentes"] = df_minas_pivot_YEAR['#INCIDENTES']/df_minas_pivot_YEAR['Conteo_Eventos'] 
df_minas_pivot_YEAR=df_minas_pivot_YEAR.reset_index()

df_minas_pivot_YEAR.to_excel(r"D:/WILSON MARTINEZ/programas/Proyectos GIT/Proyecto_minas_python/Bases_de_datos/Minas_por_año.xlsx",
                                          sheet_name='Minas_anual', encoding = 'utf-8', index = True)

#TOTALIZACION DE DATOS POR FECHAS:
df_minas_pivot_DATES=df_minas.pivot_table(index= 'Fecha del evento',values=['Conteo_Eventos','#ACCIDENTES','#INCIDENTES'],aggfunc='sum')
df_minas_pivot_DATES["P_Accidentes"] = df_minas_pivot_DATES['#ACCIDENTES']/df_minas_pivot_DATES['Conteo_Eventos'] 
df_minas_pivot_DATES["P_Incidentes"] = df_minas_pivot_DATES['#INCIDENTES']/df_minas_pivot_DATES['Conteo_Eventos'] 
df_minas_pivot_DATES=df_minas_pivot_DATES.reset_index()

df_minas_pivot_DATES.to_excel(r"D:/WILSON MARTINEZ/programas/Proyectos GIT/Proyecto_minas_python/Bases_de_datos/Minas_por_dias.xlsx",
                                          sheet_name='Minas_diario', encoding = 'utf-8', index = True)

#TOTALIZACION DE DATOS POR SEMANAS:
df_minas_pivot_WEEKS=df_minas.pivot_table(index= 'WEEKS',values=['Conteo_Eventos','#ACCIDENTES','#INCIDENTES'],aggfunc='sum')
df_minas_pivot_WEEKS["P_Accidentes"] = df_minas_pivot_WEEKS['#ACCIDENTES']/df_minas_pivot_WEEKS['Conteo_Eventos'] 
df_minas_pivot_WEEKS["P_Incidentes"] = df_minas_pivot_WEEKS['#INCIDENTES']/df_minas_pivot_WEEKS['Conteo_Eventos'] 
df_minas_pivot_WEEKS=df_minas_pivot_WEEKS.reset_index()
df_minas_pivot_WEEKS.to_excel(r"D:/WILSON MARTINEZ/programas/Proyectos GIT/Proyecto_minas_python/Bases_de_datos/Minas_por_semanas.xlsx",
                                          sheet_name='Minas_semanal', encoding = 'utf-8', index = True)


print(df_minas_pivot_WEEKS)


#---------------Graficos-------------------------------------------------------------
#Accidentes de minas
fig = plt.figure(figsize=(8,3))
ax=fig.add_subplot()
ax.set_title('Accidentes de minas semanales', fontsize=10, fontweight ="bold")
ax.plot(df_minas_pivot_WEEKS["WEEKS"],df_minas_pivot_WEEKS["#ACCIDENTES"], linewidth=2,color='red',marker='o',label='Incidentes totales')
ax.legend(loc='upper left',fontsize=10)
ax.tick_params(axis="y",labelsize=10,colors='black')
ax.tick_params(axis="x",labelsize=10,colors='black')
plt.grid(None)
plt.show()

#Incidentes de minas
fig = plt.figure(figsize=(8,3))
ax=fig.add_subplot()
ax.set_title('incidentes de minas semanales', fontsize=10, fontweight ="bold")
ax.plot(df_minas_pivot_WEEKS["WEEKS"],df_minas_pivot_WEEKS["#INCIDENTES"], linewidth=2,color='red',marker='o',label='Incidentes totales')
ax.legend(loc='upper left',fontsize=10)
ax.tick_params(axis="y",labelsize=10,colors='black')
ax.tick_params(axis="x",labelsize=10,colors='black')
plt.grid(None)
plt.show()