import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650),
                   np.random.normal(43000,100000,3650),
                   np.random.normal(43500,140000,3650),
                   np.random.normal(48000,70000,3650)],
                  index=[1992,1993,1994,1995])

df['mean'] = df.mean(axis=1)
df['errory']=df.sem(axis=1)*1.96
print(df)
index_list= df.index.tolist()
data=[ df.loc[1992], df.loc[1993], df.loc[1994], df.loc[1995] ]
errory=df.sem(axis=1)*1.96

dfmean=df['mean']
plt.figure()
plt.bar(index_list, dfmean,yerr=errory, capsize=10, width=1, color='grey', edgecolor = 'black')
ax=plt.gca()
ax.get_xaxis().set_ticks(index_list)

def onclick(event):

    horizontal_line.set_ydata(event.ydata)  #sets the y value to where you've clicked
    limit=event.ydata
    print(limit)
    colors=[]
    for x, y in zip(df['mean'], df['errory']):
        limite_sup = x+(y*0.05) #mean+5%error
        limite_inf = x-(y*0.05) #mean-5%error

        if (limit > limite_inf) and (limit < limite_sup):
            color='white'
            colors.append(color)
        elif limit > x :
            color='red'
            colors.append(color)
        elif limit < x :
            color='blue'
            colors.append(color)


    plt.bar(index_list, dfmean,yerr=errory, capsize=10, width=1, color=colors, edgecolor = 'black')
    ax=plt.gca()
    ax.get_xaxis().set_ticks(index_list)
    ax.set_title('Selected value is Y={:.3f}'.format(limit))
    plt.show()
    plt.draw()

random_value = np.random.randint(50000) #set horizontal line at random place
horizontal_line = ax.axhline(random_value, color = 'black')
plt.gcf().canvas.mpl_connect('button_press_event', onclick)
plt.show()


#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
# "sem" = "standard error of the mean" difertent a "Desviacion estandar"
# https://matplotlib.org/1.2.1/examples/pylab_examples/errorbar_demo.html
# https://www.youtube.com/watch?v=CGF9YnkNul8
# https://www.youtube.com/watch?v=7YW7x-0PmHk
