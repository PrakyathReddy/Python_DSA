"""
accept a list of dictionaries that contains JSON-RPC responses. Parse them, produce a summary in a certain format that shows only essential information.

does it matter which JSON RPC version is being used - asking so i can decide if I should be grouping by version too ?

Create a list for successful, one for failed, another to store errors. One more for latest block. Produce a new dictionary where value is decided by length of list for first 2 keys and contents of list as value for 3rd key, max value of latest block
"""
def parse_rpc_responses(json_response):
    success_count = 0

    # get number of successful entries
    error_list = []
    blocks = []
    for item in json_response:
        if "result" in item:
            success_count += 1
            blocks.append(item["result"]["block"])
        elif "error" in item:
            error_list.append(item["error"]["message"])

    return {
        "successful": success_count,
        "failed": len(json_response) - success_count,
        "errors": error_list,
        "latest_block": max(blocks) if blocks else None
    }
        





responses = [
    {"jsonrpc": "2.0", "id": 1, "result": {"block": 1000, "status": "finalized"}},
    {"jsonrpc": "2.0", "id": 2, "error": {"code": -32600, "message": "Invalid Request"}},
    {"jsonrpc": "2.0", "id": 3, "result": {"block": 1001, "status": "finalized"}},
    {"jsonrpc": "2.0", "id": 4, "error": {"code": -32601, "message": "Method not found"}},
    {"jsonrpc": "2.0", "id": 5, "result": {"block": 1002, "status": "pending"}},
]

print(parse_rpc_responses(responses))
# Expected output:
# {"successful": 3, "failed": 2, "errors": ["Invalid Request", "Method not found"], "latest_block": 1002}