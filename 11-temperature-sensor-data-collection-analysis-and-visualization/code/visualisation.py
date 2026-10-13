import matplotlib.pyplot as plt
plt.plot(df['time'], df['t1'], label="Temp Sensor 1")
plt.plot(df['time'], df['t2'], label="Temp Sensor 2")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("static/graph.png")
