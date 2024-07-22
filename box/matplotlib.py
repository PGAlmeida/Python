import matplotlib.pyplot as plt

data = [7, 2, 15, 9, 12, 4, 11, 8, 13, 6]

plt.boxplot(data)

plt.xlabel("Data")
plt.ylabel("Value")
plt.title("Boxplot with Matplotlib")

plt.show()