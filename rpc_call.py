import requests
import json

default_url = "http://127.0.0.1:26606/jsonrpc"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def rpc_call(method, params, url=default_url):
    payload = {
        "method": method,
        "params": params,
        "id": 123,
        "jsonrpc": "2.0"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    if response.status_code != 200:
        return ""

    resp = json.loads(response.text)
    return resp


def converBigInt(value):
    return str(value)
