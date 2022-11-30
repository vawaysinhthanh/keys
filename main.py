import os
import sys
import time
import base64
import requests
import datetime


def get_machine_address():
    os_type = sys.platform.lower()
    if "darwin" in os_type:
        command = """
            ioreg -ad2 -c IOPlatformExpertDevice | 
            xmllint --xpath '//key[.="IOPlatformUUID"]/following-sibling::*[1]/text()' -
        """
    elif "win" in os_type:
        command = "wmic csproduct get UUID"
    return "".join(os.popen(command).read().replace('"', "").split())

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
			dict_keys[f"{key[0]} {key[1]}"] = time.mktime(datetime.datetime.strptime(key[2], "%d/%m/%Y").timetuple())
		except:
			pass
	return dict_keys

def check_authorization(tool):
	dict_keys = get_keys()
	user = f"{get_machine_address()} {tool}"
    print(user)
	if user in dict_keys and time.time() < dict_keys[user]:
		return True
	else:
		return False

print(check_authorization("tiki-balances"))