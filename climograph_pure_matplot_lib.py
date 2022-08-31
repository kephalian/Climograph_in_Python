import numpy as np
import matplotlib.pyplot as plt
import os

####
#os.chdir('/storage/emulated/0/')
 
# set width of bar
barWidth = 0.25
fig, ax= plt.subplots(figsize =(12, 8))
 
# set height of bar
Rain=[1, 2, 9, 6, 14,151, 161, 105, 96, 108, 38, 2]
Temp=[29.3,32.2, 35,37.3, 36.4,36.4, 25.3,25.3,26.7,28.4,28,28]
Humi=[44, 36,33,37,51,77,86, 88, 85,71,60,52]
 
# Set position of bar on X axis
br1 = np.arange(len(Rain))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
 
# Make the plot
plt.bar(br1, Rain, color ='red', width = barWidth,
        edgecolor ='grey', label ='Rainfall mm')
        
#df['data'].plot(kind='line', marker='*', color='black', ms=10)
#Temp.plot(secondary_y=True)        
#plt.bar(br2, Temp, color ='g', width = barWidth, edgecolor ='grey', label ='Temperature °C')
plt.bar(br3, Humi, color ='yellow', width = barWidth,
        edgecolor ='grey', label ='Humidity %')


#ax2 = ax.twinx()
#ax2.plot(Temp, color='green', marker='o')
#df[['sales_gr','net_pft_gr']].        
#plt.plot(Temp, color='green', marker='o')
#plt.title('Unemployment Rate Vs Year', fontsize=14)
#plt.xlabel('Year', fontsize=14)
#plt.ylabel('Unemployment Rate', fontsize=14)
plt.grid(True)
plt.legend()
# Adding Xticks
plt.xlabel('Climograph', fontweight ='bold', fontsize = 15)
plt.ylabel('Rainfall in millimeters and Humidity in %', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Rain))],
        ['Jan', 'Feb', 'March', 'April','May','June', 'July','Aug','Sep', 'Oct', 'Nov', 'Dec'])
        
ax2 = ax.twinx()  
# instantiate a second axes that shares the same x-axis

color = 'navy'
ax2.set_ylabel('Temperature °C', color=color) 
 # we already handled the x-label with ax1
ax2.plot(Temp, color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

 


fig.tight_layout()
plt.savefig('Climatograph_chiplun.png', dpi=400)
plt.show()
