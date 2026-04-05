import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data.csv")

top_repos = df.sort_values(by="stars", ascending=False).head(10)

plt.figure()
plt.barh(top_repos["name"], top_repos["stars"])
plt.xlabel("Stars")
plt.ylabel("Repository")
plt.title("Top 10 Trending GitHub Repositories")

plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("trend_visualization.png")

plt.show()
