from rpc_call import rpc_call


# not safe, account private key is not encrypted
# deprecate later
def new_account(name):
    resp = rpc_call('owner.GenerateNewAccount', {'name': name})
    return resp['result']


def addresses():
    resp = rpc_call('owner.ListAccountAddresses', {})
    return resp["result"]["addresses"]


def sign(rawTx, address):
    resp = rpc_call('owner.SignWithAddress', {"rawTx": rawTx, "address": address})
    return resp["result"]
