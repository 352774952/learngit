import requests
import json

# 格式化json输出


def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)


url = 'https://tianqiapi.com/api'
params = {
    "city": "北京"
}
response = requests.request("post", url, params = params)
result = json.loads(response.text)
js = result['cityid']
print(js)


