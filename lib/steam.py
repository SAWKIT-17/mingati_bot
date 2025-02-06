import requests
from bs4 import BeautifulSoup

def get_free_games():
    url = "https://store.steampowered.com/search/?maxprice=free&specials=1&ndl=1"
    headers = {"User-agent": "Mozilla/5.0"}
    response = requests.get(url, headers)
    soup = BeautifulSoup(response.text, "html.parser")

    games = []
    print("🔎 Recherche de jeux gratuit sur Steam...")
    for result in soup.find_all("a", class_="search_result_row"):
        title_tag = result.find("span", class_="title")
        if title_tag:
            title = title_tag.text
            link = result["href"]
            games.append((title, link))

    print(f"✅ Recherche terminé. Jeux trouvés :\n {games}")
    return games