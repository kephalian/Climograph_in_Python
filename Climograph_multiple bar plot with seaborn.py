import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

####
#os.chdir('/storage/emulated/0/')
 
sns.set_style("darkgrid")
#sns.set_palette('Reds')

fig, ax= plt.subplots(figsize =(20, 10))
ax2 = ax.twinx()
# set height of bar
Rain=[1, 2, 9, 6, 14,151, 161, 105, 96, 108, 38, 2]
Temp=[29.3,32.2, 35,37.3, 36.4,36.4, 25.3,25.3,26.7,28.4,28,28]
Humi=[44, 36,33,37,51,77,86, 88, 85,71,60,52]
months= ['Jan', 'Feb', 'March', 'April','May','June', 'July','Aug','Sep', 'Oct', 'Nov', 'Dec']


#"RdBu_r")
#"gist_rainbow")


#sns.lineplot(Humi)
# Humi)
#sns.barplot(months, Humi)




ax.set_xlabel('Climograph of Sawarde (drawn by authors)', fontweight ='bold', fontsize = 15)
ax.set_ylabel('Rainfall [bars] in millimeters and Humidity [X] Blue line in %', fontweight ='bold', fontsize = 15)
#plt.xticks([r + barWidth for r in range(len(Rain))],
#        ['Jan', 'Feb', 'March', 'April','May','June', 'July','Aug','Sep', 'Oct', 'Nov', 'Dec'])
        

# instantiate a second axes that shares the same x-axis

#color = 'navy'
ax2.set_ylabel('Temperature °C [o] Orange',fontweight ='bold', fontsize = 15) #color=color) 
 # we already handled the x-label with ax1
#sns.lineplot(data=Temp)
ax.plot(Humi, color='royalblue', marker='x',linewidth=3)

ax2.plot(Temp, color='darkorange', marker='o', linewidth=3)

sns.barplot(x=months, y=Rain, palette="Dark2")
plt.legend()
#ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()

#add legend

plt.savefig('Climatograph_chiplun3.png', dpi=400)
plt.show()