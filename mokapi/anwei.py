import requests

def anwei():
	url = "https://v.api.aa1.cn/api/api-wenan-anwei/index.php?type=json"

	response = requests.get(url)
	data = response.json()

	anwei = data["anwei"]
	print(anwei)