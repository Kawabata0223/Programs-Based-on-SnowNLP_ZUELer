import json
import csv
import requests
import time
from fake_useragent import UserAgent
import os

# 获取网页响应的json文件
def get_html(url):
    headers = {
        "User-Agent": UserAgent().random,
        "Referer": "https://weibo.com/"
    }
    cookies = {
        "cookie": "XSRF-TOKEN=XaDTHukbo_9ceDlHubg0YUVn; SUB=_2A25IPPiLDeRhGeFN7FcU8SrPyj-IHXVrMHRDrDV8PUNbmtB-LUqtkW9NQ8xs_zg2qVv5KD7fA_gitxJLaJQsqidj; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhRmGUpZbrV0HPsqUxcq0rm5JpX5KzhUgL.FoM0S0-feKB0eKe2dJLoIEXLxK.LBozLBonLxKqL1KnLB-qLxK-L1KeLB.2LxKBLBo.LBoeLxKMLBo2LB.zt; ALF=1729739867; SSOLoginState=1698203867; WBPSESS=bE-DSIeJx2-KcY3Ei0BWA1o0YvVu8ngn1V7S6gVQrc7pumI6EQy9mTFqnMJpsHOhG7il_mnm50lq3AqqE_CahbltDZCvD2945g6IsZhHN1pwYs3bmjEjRa5wpD8J7PwnXUoUVDCMLXcu7osrISJfbQ=="
    }
    response = requests.get(url, headers=headers, cookies=cookies)
    time.sleep(3)
    return response.text


def get_string(text):
    t = ''
    flag = 1
    for i in text:
        if i == '<':
            flag = 0
        elif i == '>':
            flag = 1
        elif flag == 1:
            t += i
    return t


# 保存评论
def save_text_data(filename,text_data):
    text_data = get_string(text_data)
    with open(filename, "a", encoding="utf-8", newline="")as fi:
        fi = csv.writer(fi)
        fi.writerow([text_data])




# 获取一级评论
def get_first_comments(filename, weibo_id):

    url = f'https://weibo.com/ajax/statuses/show?id={weibo_id}'
    header = {
        'user-agent': UserAgent().random
    }
    res = requests.get(url=url, headers=header)
    json_data = res.json()
    weibo_id = json_data['id']
    user_id = json_data['user']['idstr']
    print(id, user_id)
    max_id = ''

    page = 0
    while max_id != 0:
        url = f'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id={weibo_id}&is_show_bulletin=2&is_mix=0&max_id={max_id}&count=10&uid={user_id}'
        response = get_html(url.format(weibo_id, max_id, user_id))
        content = json.loads(response)
        content_list = content['data']
        max_id = content['max_id']
        cnt = 0
        for content in content_list:
            comment_content = content['text']
            save_text_data(filename, comment_content)
            cnt += 1
        page += 1
        print(f'已保存{page}页')
        if page >=10:break



if __name__ == '__main__':

    weibo_ids = ["5009594490819403"] # 目标微博的id
    filename = "files/data.csv"
    if os.path.exists(filename):
        os.remove(filename)
    for weibo_id in weibo_ids:
        print("爬取开始")

        try:
            get_first_comments(filename,weibo_id)
            print("爬取完成")
        except Exception as e:
            print("爬取失败")
            print(e)
            continue






