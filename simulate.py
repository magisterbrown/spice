import subprocess
import pandas as pd
import matplotlib.pyplot as plt

res = subprocess.run(["./ngspice", "./inverter.cir"], stdout=subprocess.PIPE)
output = res.stdout.decode()
rows = output.split('\n')
prep = map(lambda x: x.split('\t')[:-1], filter(lambda x: len(x) and x[0].isdigit(), rows))
df = pd.DataFrame(prep, columns=['index', 'time', "out", 'ain', "bin"]).set_index('index').astype("float")
print(df)
ax = plt.subplot()
ax.plot(df['time'], df['ain'], label="ain", linewidth=3)
ax.plot(df['time'], df['bin'], label="bin", linewidth=2)
ax.plot(df['time'], df['out'], label="out", linewidth=1)
ax.legend()
plt.show()
