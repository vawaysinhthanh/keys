import base64
import requests


def get_keys():
	user = "mrshaw01"
	repo_name = "keys"
	path_to_file = "keys.txt"
	url = f'https://api.github.com/repos/{user}/{repo_name}/contents/{path_to_file}'
	res = requests.get(url)
	keys = base64.b64decode(res.json()["content"]).decode("utf-8")
	dict_keys = {}
	for key in keys.split("\n"):
		key = key.strip().split()
		try:
			dict_keys[key[0]] = {}
			dict_keys[key[0]]['tool'] = key[1]
			dict_keys[key[0]]['date'] = key[2]
		except:
			pass
	return dict_keys

dict_keys = get_keys()
print(dict_keys)