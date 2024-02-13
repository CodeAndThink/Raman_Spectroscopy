import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
colors = ['red', 'blue', 'green', 'purple', 'orange', 'olive', 'black', 'cyan', 'magenta', 'yellow']
data = pd.read_csv('Ten_labels/Tenlabels_RamanData.csv', header=None)
data = data.to_numpy()
x_axit = np.arange(0, len(data[0]))
for i in range(len(data)):
    y_axit = data[i]
    plt.plot(x_axit, y_axit, color=random.choice(colors), label='i')

plt.xlabel('Wave')
plt.ylabel('Intensity')
plt.title('graph_name')
plt.xticks(x_axit[::50],  rotation='vertical')
plt.show()

