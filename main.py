import time
import traceback
from json import loads as json_loads
from json import dumps as json_dumps

from json import dumps as json_dumps

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

### 以上无需修改

### 以下一定需要修改
Cookie = r''
Cookie = r''

studentCode = r''


### 以下可能需要修改
url_DailyFeedback = r''
url_DailyFeedback = r'http://ce.fudan.edu.cn/API/Admin/DailyFeedback/FeedbackStudent.ashx?action=query&semester=2021-2022-1&searchName=&type=1&v=1638193860058&index=1&psize=200&orderby=&col=&ordertype=&order='

url_mytask = r''
url_mytask = r'http://ce.fudan.edu.cn/API/Students/QuestinlistByStu.ashx?action=querymytask&type=-1&category=1&name=&v=1638193793285&index=1&psize=10&orderby=&col=&ordertype=&order='

uid = r'2021-2022-1-' + studentCode
### 以下无需修改

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "ce.fudan.edu.cn",
    "Referer": "http://ce.fudan.edu.cn/Admin/DailyFeedback/Student/DailyFeedbackList.aspx",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

headers['Cookie'] = Cookie

url_home = r'http://ce.fudan.edu.cn/admin/Home.aspx'
SubjectId = r'f131dcec-1b7b-11ec-9b3f-00505680e0d1'
qid = r'c0b3a16592ed4c1399f2a3e4ff31f3c8'
pageid = r'f131be95-1b7b-11ec-9b3f-00505680e0d1'
SubjectGUID = r"f131dcaf-1b7b-11ec-9b3f-00505680e0d1"
SubjectItemGUID = r'f131de32-1b7b-11ec-9b3f-00505680e0d1'

def get(url):
    ret = requests.get(url, headers = headers)
    return ret.json()

def post(url, data):
    ret = requests.post(url, headers = headers, data = data)
    return ret.json()

def reverseGeo(geo_api_info):
    res = json_dumps(geo_api_info, ensure_ascii=False)
    res = res.replace('", "','","')
    res = res.replace('": ','":')
    res = res.replace(', "',',"')
    res = res.replace('}, {','},{')
    return res

def try_call(call, *arg, **kw):
    try:
        call(*arg, **kw)
    except:
        print(traceback.format_exc())

def get_task(url):
    ret = get(url)
    ret = ret['data']
    ret = ret['ItemList']
    return ret

def workontask(task):
    hd = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": "11860",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": headers['Cookie'],
    "DNT": "1",
    "Host": "ce.fudan.edu.cn",
    "Origin": "http://ce.fudan.edu.cn",
    "Referer": "http://ce.fudan.edu.cn/q.aspx?id=14815090&sqid=0137f2f15ece4a22a855e82b13348a7e&type=5&stepseq=3dbdad46c1ae425abcef3708ad3bd4e7&targettype=2&targetcode=64ea46ef8dcc476b96d2ef083731df9e&tag=0137f2f15ece4a22a855e82b13348a7e_5_64ea46ef8dcc476b96d2ef083731df9e_2_2021-2022-1-MED130190_0_14815090&beginTime=2021-11-29%2008:00&endTime=2021-12-26%2023:59&previewTime=2021-10-18%2011:09&name=2021%E5%B9%B4%E7%A7%8B%E5%AD%A3%E6%9C%9F%E6%9C%AB%E8%AF%84%E6%95%99-%E7%90%86%E8%AE%BA%E8%AF%BE-%E5%9F%BA%E7%A1%80%E5%8C%BB%E5%AD%A6%E7%A0%94%E7%A9%B6%E5%85%A5%E9%97%A8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }
    null = None
    curpage_result_str = [
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e404ba-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e408c5-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":3
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e40674-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e40996-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":3
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e40653-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e40a1a-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":4
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e4045f-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e40b9b-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":3
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e405cd-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e40c4b-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":6
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e40518-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e40cf2-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":6
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e40691-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e40d99-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":6
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e4056f-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e40e3d-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":6
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e4043f-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e410b7-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":3
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e40626-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e40f91-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":8
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e406e6-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e41161-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":8
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e4049b-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e41209-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":0
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e406ae-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e412b6-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":0
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e404e8-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e413d4-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":4
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"c7692456-dcee-4e0f-a193-1d4004d9fbf6",
    "SubjectItemGUID":"de623301-55d4-482d-b89b-c0fedf93815a",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":0
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"a57319a2-49e0-4912-a076-f89a6c87d9e3",
    "SubjectItemGUID":"76ace005-34c7-4b8b-9b26-fd9e7de6db12",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":0
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"c7767a48-206b-4b3b-865e-321fdbfc0782",
    "SubjectItemGUID":"6f0e6126-2a50-40d8-ad6b-4243288661a5",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":0
    },
    {
    "ResultValue":3,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e4047d-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e414e3-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":0
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e405f9-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e41536-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":0
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e4059b-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e41604-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":"5"
    },
    {
    "ResultValue":2,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e4059b-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e41630-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":"5"
    },
    {
    "ResultValue":3,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e4059b-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e41657-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":"5"
    },
    {
    "ResultValue":4,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e4059b-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e41682-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":"5"
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e406ca-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e417f3-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":10
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e40541-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e4186e-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "ResultScore":10
    },
    {
    "ResultValue":1,
    "QuestionnaireGUID":null,
    "SubjectPageGUID":"75e40182-3147-11ec-9b3f-00505680e0d1",
    "SubjectGUID":"75e40703-3147-11ec-9b3f-00505680e0d1",
    "SubjectItemGUID":"75e41c33-3147-11ec-9b3f-00505680e0d1",
    "TabPageType":"1",
    "TabPageCode":"",
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":"",
    "OpenText":"很好",
    "ResultScore":0
    }
    ]
    template = {
    "action": "saveAnswer",
    "qid": "83582e2baeb946608807ae29500653ab",
    "sqid": task['GUID'],
    "pageid": "finish",
    "next_pageid": "75e40182-3147-11ec-9b3f-00505680e0d1",
    "curpage_result_str": reverseGeo(curpage_result_str),
    "pagecount": "2",
    "stepcount": "1",
    "pid": task['Id'],
    "tag": task['Tag'],
    "type": "",
    "showname": "0",
    "answerTime": "",
    "evalTime": "0",
    "tcode": "",
    "updated": "",
    "edit": "",
    "pageorder": "1",
    "uid": uid,
    "steptype": "",
    "targettype": "2",
    "targetcode": task['TargetCode'],
    "stepseq": task['StepSeq']
    }
    # print(template)
    api = r'http://ce.fudan.edu.cn/api/webquestion.ashx'
    ret = requests.post(api, headers = hd, data = template).json()
    print(ret['status'])

def workondaily(task):
    template = {
    "action": "insert",
    "content": "谢谢老师！",
    "subjectId": SubjectId,
    "questionnaireId": task['QuestionnaireId'],
    "teacherCode": task['TeacherCode'],
    "studentCode": studentCode,
    "courseCode": task['CourseCode'],
    "classCode": task['ClassCode'],
    "departmentCode": task['DepartmentCode']
    }
    api = r'http://ce.fudan.edu.cn/API/Admin/DailyFeedback/DailyFeedback.ashx'
    ret = post(api, template)
    print(ret['message'])

def workonorder(task):
    api = r'http://ce.fudan.edu.cn/api/webquestion.ashx'
    curpage_result_str = {
    "ResultValue":1,
    "QuestionnaireGUID": task['QuestionnaireId'],
    "SubjectPageGUID": pageid,
    "SubjectGUID": SubjectGUID,
    "SubjectItemGUID":SubjectItemGUID,
    "ResultScore":100,
    "TabPageType":2,
    "TabPageCode":task['TeacherCode'],
    "AnswerTime":"",
    "EvalTime":"0",
    "TeacherCode":task['TeacherCode']
    }
    
    template = {
    "action": "saveAnswer",
    "qid": qid,
    "sqid": task['QuestionnaireId'],
    "pageid": pageid,
    "next_pageid": "finish",
    "curpage_result_str": reverseGeo([curpage_result_str]),
    "pagecount": "1",
    "stepcount": "1",
    "pid": "",
    "tag": task['CourseCode'],
    "type": "",
    "showname": "0",
    "answerTime": "",
    "evalTime": "0",
    "tcode": task['TeacherCode'],
    "pageorder": "1",
    "uid": uid,
    "steptype": "",
    "targettype": "2",
    "targetcode": task['ClassCode'],
    "stepseq": task['StepSeq']
    }
    
    hd = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": headers['Cookie'],
    "DNT": "1",
    "Host": "ce.fudan.edu.cn",
    "Origin": "http://ce.fudan.edu.cn",
    "Referer": "http://ce.fudan.edu.cn/q_dailyFeedback.aspx?tasktype=100&targettype=2&courseCode=2021-2022-1-MED130190&tcode=01674&targetcode=64ea46ef8dcc476b96d2ef083731df9e&classAlias=MED130190.01&sqid=6049356d9ea049dbb0e990207364f1dc&qid=6049356d9ea049dbb0e990207364f1dc&departmentCode=2021-2022-1-86&isMoreTeacher=true&courseName=%E5%9F%BA%E7%A1%80%E5%8C%BB%E5%AD%A6%E7%A0%94%E7%A9%B6%E5%85%A5%E9%97%A8&teacherName=%E7%8E%8B%E6%9D%BE%E6%A2%85&stepseq=3996d4e3055d4ae8a33d3381f268a157&semester=2021-2022-1&next=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }
    # print(template)
    ret = requests.post(api, headers = hd, data = template).json()
    print(ret['status'])

def finishDaily():
    alltask = get_task(url_DailyFeedback)
    for one in alltask:
        try_call(workondaily, one)
        try_call(workonorder, one)

def finishTask():
    alltask = get_task(url_mytask)
    for one in alltask:
        try_call(workontask, one)

finishDaily()
finishTask()
