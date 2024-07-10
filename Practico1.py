"""
Práctico 1 Diplomatura Datos
Clara Cabrera - Marianela Luján - Nicolás Salles
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Cargamos la base de datos
file= 
datos = pd.read_csv(file)
datos.head()
datos.info()

"""
Descripción de variables:
male: sexo, codificado con 1 (Hombres) y 0 (Mujeres)
age: edad en años
education: Nivel educativo
currentSmoker: fumador actual (1:si, 0:no)
cigsPerDay: cigarrillos por día
BPMeds: medicación para la presión arterial (1:si, 0:no)
prevalentStroke: accidente cerebrovascular anteriormente (1:si, 0:no)
prevalentHyp: hipertensión (1:si, 0:no)
diabetes: diabetes (1:si, 0:no)
totChol: nivel de colesterol
sysBP: presión arterial sistólica
diaBP: presión arterial diastólica
BMI: índice de masa corporal
heartRate: ritmo cardiaco
glucose: nivel de glucosa
TenYearCHD: riesgo de enfermedad coronaria a 10 años (1:si, 0:no)

Tenemos entonces las siguientes variables categóricas: male, currentSmoker, BPMeds, prevalentStroke, prevalentHyp, diabetes, education, TenYearCHD;
y las variables numericas: age, cigsPerDay, totChol, sysBP, diaBP, BMI, heartRate, glucose.
"""
#Procedemos a eliminar la variable educación:
datos=datos.drop(columns=['education'])
datos.head()
"""
Analisis descriptivo
Veamos ahora como algunas de estas variables se relacionan con nuestra variable de interes TenYearCHD: riesgo de contraer enfermedad coronaria a 10 años.

Empezamos con la distribución de las variables categóricas respecto de TenYearCHD:
"""
fig, ax = plt.subplots(2, 3, figsize=(15, 8))

# Sexo respecto a riesgo de enfermedad coronaria a 10 años
sns.countplot(x='male', hue = 'TenYearCHD', data=datos , ax=ax[0,0])
ax[0,0].set_title("sexo por riesgo de EC")

# Fumador actual respecto a riesgo de enfermedad coronaria a 10 años
sns.countplot(x='currentSmoker', hue = 'TenYearCHD', data=datos , ax=ax[0,1])
ax[0,1].set_title("fumador actual por riesgo de EC")

# Medicacion para la presion respecto a riesgo de enfermedad coronaria a 10 años
sns.countplot(x='BPMeds', hue = 'TenYearCHD', data=datos , ax=ax[0,2])
ax[0,2].set_title("medicacion para presión por riesgo de EC")

# Accidente cerebrovascular anteriormente respecto a riesgo de enfermedad coronaria a 10 años
sns.countplot(x='prevalentStroke', hue = 'TenYearCHD', data=datos , ax=ax[1,0])
ax[1,0].set_title("acv por riesgo de EC")

# Hipertension respecto a riesgo de enfermedad coronaria a 10 años
sns.countplot(x='prevalentHyp', hue = 'TenYearCHD', data=datos , ax=ax[1,1])
ax[1,1].set_title("hipertensión por riesgo de EC")

# Diabetes respecto a riesgo de enfermedad coronaria a 10 años
sns.countplot(x='diabetes', hue = 'TenYearCHD', data=datos , ax=ax[1,2])
ax[1,2].set_title("diabetes por riesgo de EC")


fig.suptitle('')
plt.subplots_adjust(hspace=0.3)
plt.show()

"""
Veamos el riesgo de enfermedad coronario segun variables numericas:
"""

fig, ax = plt.subplots(4, 2, figsize=(15, 15))


# Edad según presencia o no de riesgo de enfermedad coronaria a 10 años
datos.boxplot(column='age', by = 'TenYearCHD', ax=ax[0,0])
ax[0,0].set_title("Edad según riesgo de EC")

# Cigarrillos por día según presencia o no de riesgo de enfermedad coronaria a 10 años
datos.boxplot(column='cigsPerDay', by = 'TenYearCHD', ax=ax[0,1])
ax[0,1].set_title("Cigarrillos por día según riesgo de EC")

# Colesterol total según presencia o no de riesgo de enfermedad coronaria a 10 años
datos.boxplot(column='totChol', by = 'TenYearCHD', ax=ax[1,0])
ax[1,0].set_title("Colesterol total según riesgo de EC")

# Presión arterial sistólica según riesgo o no de riesgo de enfermedad coronaria a 10 años
datos.boxplot(column='sysBP', by = 'TenYearCHD', ax=ax[1,1])
ax[1,1].set_title("Presión arterial sistólica según riesdo de EC")

# Presión arterial diastólica según presencia o no de riesgo de enfermedad coronaria a 10 años
datos.boxplot(column='diaBP', by = 'TenYearCHD', ax=ax[2,0])
ax[2,0].set_title("Presión arterial diastólica según riesgo de EC")

# indice de masa corporal según presencia o no de riesgo de enfermedad coronaria a 10 años
datos.boxplot(column='BMI', by = 'TenYearCHD', ax=ax[2,1])
ax[2,1].set_title("BMI según riesgo de EC")

# Glucosa según presencia o no de riesgo de enfermedad coronaria a 10 años
datos.boxplot(column='glucose', by = 'TenYearCHD', ax=ax[3,0])
ax[3,0].set_title("glucosa según riesgo EC")

# Ritmo cardiaco según presencia o no de riesgo de enfermedad coronaria a 10 años
datos.boxplot(column='heartRate', by = 'TenYearCHD', ax=ax[3,1])
ax[3,1].set_title("ritmo cardiaco según riesgo EC")

fig.suptitle('')
plt.subplots_adjust(hspace=0.3)
plt.show()

"""
Podemos ver también la matriz de correlaciones entre estas variables numéricas:
"""
corr_datos = datos[['age', 'cigsPerDay', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_datos, annot=True)
plt.show()

"""
REVISAR :
De los graficos anteriores podemos observar que:
La mayoría de los hombres tienen un mayor riesgo de enfermedad coronaria a 10 años en comparación con las mujeres. 
Los fumadores actuales muestran una mayor prevalencia de riesgo de enfermedad coronaria a 10 años. 
Las personas que toman medicación para la presión arterial, con antecedentes de acv, hipertensión y diabetes presentan un mayor riesgo de enfermedad coronaria a 10 años. 
La edad muestra una tendencia a ser mayor en aquellos con riesgo de enfermedad coronaria a 10 años. 
Los niveles de colesterol total, presión arterial sistólica, presión arterial diastólica y glucosa son más altos en aquellos con riesgo de enfermedad coronaria a 10 años.
No se observa una gran diferencia en el índice de masa corporal y la frecuencia cardíaca entre los dos grupos. 
Existe una correlación positiva notable entre la presión arterial sistólica y diastólica. 
La edad muestra una correlación positiva con la presión arterial sistólica y diastólica, lo que indica que la presión arterial tiende a aumentar con la edad. 
El índice de masa corporal no muestra una fuerte correlación con las otras variables. 
Esto sugiere que factores como el género, fumar, la edad, la presión arterial, el colesterol y la glucosa están relacionados con un mayor riesgo de enfermedad coronaria a 10 años.
"""
