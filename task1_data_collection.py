import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://github.com/trending"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

repos = []
repo_list = soup.find_all("article", class_="Box-row")

for repo in repo_list:
    name = repo.h2.a.text.strip().replace("\n", "").replace(" ", "")
    description = repo.p.text.strip() if repo.p else "No description"
    stars = repo.find("a", href=lambda x: x and x.endswith("/stargazers"))
    stars = stars.text.strip() if stars else "0"

    repos.append({
        "name": name,
        "description": description,
        "stars": stars
    })

df = pd.DataFrame(repos)
df.to_csv("raw_data.csv", index=False)

print("Data collected and saved to raw_data.csv")