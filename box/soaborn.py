import seaborn as sns
import matplotlib.pyplot as plt

data = [7, 2, 15, 9, 12, 4, 11, 8, 13, 6]

sns.boxplot(data=data)

data = {"category": ["A", "B", "A", "A", "B", "A", "A", "B", "B", "A"], "values": data}
sns.boxplot(x="category", y="values", data=data)

plt.show()