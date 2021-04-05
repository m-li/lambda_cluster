import cloudpickle

def handler(event, context):
    func = cloudpickle.loads(event["func"].encode('latin1'))
    args = event["args"]
    r = func(*args)
    return {"statusCode": 200, "results": r}
