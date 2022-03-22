import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

#Agregar base de datos de minas del gobierno de colombia
df_minas = pd.read_excel("D:/WILSON MARTINEZ/programas/python/Analisis_Minas/Base_minas_colombia_analisis.xlsx",sheet_name="Evento_minas_RAW")
#Arreglo de caracteres con espacio el la columna "presunto actor responsable"
df_minas['Presunto actor responsable']=df_minas['Presunto actor responsable'].str.strip(' ')
