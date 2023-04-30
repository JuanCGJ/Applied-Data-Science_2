# link base de datos
# https://www.dane.gov.co/index.php/estadisticas-por-tema/mercado-laboral/empleo-y-desempleo
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html
# https://matplotlib.org/stable/gallery/ticks_and_spines/major_minor_demo.html
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#elimino datos desde la celda 1 a 247
#utilizo datos desde la celda 247 hasta 253. (descarto # celdas que no necesito, total 766-5=761)
df=pd.read_excel("unemployment_rate.xlsx", sheet_name = "areas trim movil", header=0,
                keep_default_na=False, usecols="A,HV:HY,IH:IK", skiprows=247, skipfooter=761)

df.rename(columns={'Concepto': 'Concepts', 'Unnamed: 230': '2020', 'Unnamed: 231': '2020',
'Unnamed: 232': '2020', 'Unnamed: 241': '2021', 'Unnamed: 242': '2021', 'Unnamed: 243': '2021',
'Unnamed: 244': '2021'}, inplace=True)

df.iloc[1,0]='Peopple(%) able to work'
df.iloc[2,0]='Global Rate participation(GRP)'
df.iloc[3,0]='Occupation Rate(OR)'
df.iloc[4,0]='Unemployment Rate(UR)'

df.replace('\*','', regex=True, inplace=True) #reemplazo asterisco por esapcio ' '
df.iloc[0,0:]=df.iloc[0,0:].str.strip()       #retiro espacios de la derecha
print(df)

xlabels=[]
for n in df.iloc[0,1:5]:
    xlabels.append(n)

ylabels2020=[]
for i in df.iloc[4,1:5]:
    ylabels2020.append(i)

ylabels2021=[]
for j in df.iloc[4,5:10]:
    ylabels2021.append(j)

plt.figure()
# # plot the linear data and the exponential data
# plt.plot(xlabels,ylabels2020, '-*b', xlabels,ylabels2021, '-*g')

x_axis = np.arange(len(xlabels))
bars1= plt.bar(x_axis - 0.2, ylabels2020, 0.4, label='2020', color='b', edgecolor = 'black')
bars2= plt.bar(x_axis + 0.2, ylabels2021, 0.4, label='2021', color='violet', edgecolor = 'black')
plt.ylabel('Rate %', rotation='horizontal', position=(0,0.7))
plt.xlabel('Shifted Quarters')
plt.title('Unemployment Rate/Semester1  (Manizales, Colombia).')
plt.xticks(x_axis, xlabels)
plt.legend()
# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(axis='both', which='major', top=False, bottom=False,
                left=False, right=False, labelleft=False, labelbottom=True)

# remove borders
for spine in plt.gca().spines.values():
    spine.set_visible(False)
# direct label each bar with Y axis values
for bar in bars1:
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str("{0:.2f}".format(bar.get_height())) + '%',
                 ha='center', color='w', fontsize=9)

for bar in bars2:
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str("{0:.2f}".format(bar.get_height())) + '%',
                 ha='center', color='black', fontsize=9)
plt.show()

# print(df.columns)
