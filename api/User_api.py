import requests
import json

import setting

#获取全组织
def get_user_list(projectId,departmentId):
    payload = json.dumps({
        "pageSize": 0,
        "pageNum": 1,
        "orderByColumn": "",
        "isAsc": "",
        "projectId": projectId,
        "userStatus": 1,
    })
    headers = {
        'Authorization': setting.sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", setting.test_url + '/user/pagedNormalUserList', headers=headers, data=payload)
    print(response.json())

    return response.json()

def get_user_dpat_user_list(ProjectId,DepartmentId):
    payload = json.dumps({
        "pageSize": 50,
        "pageNum": 1,
        "projectId": ProjectId,
        "departmentId": DepartmentId
    })
    headers = {
        'Authorization': setting.sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", setting.test_url + '/user/getDepartmentUsers', headers=headers, data=payload)
    print(response.json())
    return response.json()