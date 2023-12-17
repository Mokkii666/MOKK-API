import requests
def liss():
    url = "https://jx.iqfk.top/60s.php?key=54K55paw6Iqx6Zuo"
    response = requests.get(url)
    data = response.json()

    news = data["data"]["news"]

    for item in news:
        print(item)
