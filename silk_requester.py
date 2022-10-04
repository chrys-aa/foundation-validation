import requests

headers = { 
        "Authorization": f"Bearer test",
        "Accept": "application/vnd.github+json"
    }

def getExecutionInfo(executionId):
    param = {'executionPlanRunId' : executionId}
    try:
        response = requests.get(f"http://192.168.15.6:3000/plan",headers=headers, params=param, timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print("Erro na requisição")
        return 0

def getExecutionDetail(executionId):
    param = {'executionPlanRunId' : executionId}
    try:
        response = requests.get(f"http://192.168.15.6:3000/planDetail",headers=headers, params=param, timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print("Erro na requisição")
        return 0