import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("../dataset/cleaned_house_prices.csv")


# 1. Price Distribution
plt.figure(figsize=(8, 5))

plt.hist(df["price"], bins=20)

plt.title("House Price Distribution")
plt.xlabel("House Price")
plt.ylabel("Number of Houses")

plt.savefig("../outputs/price_distribution.png")

plt.show()


# 2. Area vs Price
plt.figure(figsize=(8, 5))

plt.scatter(df["area"], df["price"])

plt.title("Area vs House Price")
plt.xlabel("Area")
plt.ylabel("House Price")

plt.savefig("../outputs/area_vs_price.png")

plt.show()


# 3. Correlation Heatmap
numeric_data = df.select_dtypes(include="number")

correlation = numeric_data.corr()

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.savefig("../outputs/correlation_heatmap.png")

plt.show()

print("All visualizations created successfully!")