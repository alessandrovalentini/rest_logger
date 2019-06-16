from flask import request

def getQueryParam(paramName):
    # user = ""
    user = request.args.get(paramName)
    if user is not None:
        return user
    else:
        return "please use query param"