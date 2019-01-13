from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import image



# Fixing random state for reproducibility
np.random.seed(19680701)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
decisions = ('Si', 'No')
y_pos = np.arange(len(decisions))
performance = 3 + 10 * np.random.rand(len(decisions))
error = np.random.rand(len(decisions))

ax.barh(y_pos, performance, xerr=error, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(decisions)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Resultado')
ax.set_title('¿Deberiamos obligar a estudiar ingles desde niños?')


fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('pruebaFinal.png', dpi=100)

im = Image.open("pruebaFinal.png")
bg=Image.new("RGB", im.size, (255,255,255))
bg.paste(im,(0,0),im)
bg.save("Formato.jpg",quality=95)