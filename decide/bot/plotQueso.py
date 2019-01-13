import matplotlib.pyplot as plt
from PIL import Image


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'PP', 'Ciudadanos', 'Podemos', 'PSOE'
sizes = [15, 30, 25, 30]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Ciudadanos')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#plt.show()

fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('pruebaQueso.png', dpi=100)

im = Image.open("pruebaQueso.png")
bg=Image.new("RGB", im.size, (255,255,255))
bg.paste(im,(0,0),im)
bg.save("Queso.jpg",quality=95)

