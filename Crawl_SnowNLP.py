import re
import requests
import time
import csv


def getArticleId(id_str):
    """
    :param id_str: 需要解密的id字符串
    :return:
    """
    url_id = "https://weibo.com/ajax/statuses/show?id={}".format(id_str)
    resp_id = requests.get(url_id, headers=headers)
    if resp_id is None:
        return 0
    article_id = resp_id.json()["id"]
    return article_id


def get_one_page(params):
    """
    :param params: get请求需要的参数，数据类型为字典
    :return:  max_id：请求所需的另一个参数
    """
    url = "https://weibo.com/ajax/statuses/buildComments"
    resp = requests.get(url, headers=headers, params=params)

    data_list = resp.json()["data"]

    for data in data_list:
        # 拓展内容
        # gender = '男' if data["user"]["gender"].strip() == 'm' else '女'

        data_dict = {
            # 拓展内容
            # "用户名称": data["user"]["screen_name"],
            # "性别": gender,
            # "粉丝数量": data["user"]["followers_count"],
            # "评论时间":data["created_at"].replace("+0800", ""),
            # "IP属地": data["source"][2:],
            # "点赞数量":data["like_counts"],
            "评论内容":data["text_raw"].strip().replace('\n', ''),

        }
        global comment_number
        comment_number = comment_number + 1
        print("已经爬到的评论数：", comment_number)
        # print(
        #     #拓展内容
        #     # f'用户名称：{data_dict["用户名称"]}\n'
        #     # f'性别：{data_dict["性别"]}\n'
        #     # f'粉丝数量：{data_dict["粉丝数量"]}\n'
        #     # f'评论时间：{data_dict["评论时间"]}\n'
        #     # f'IP属地：{data_dict["IP属地"]}\n'
        #     # f'点赞数量：{data_dict["点赞数量"]}\n'
        #     f'评论内容；{data_dict["评论内容"]}\n'
        # )
        #print("=" * 90)
        writer.writerow(data_dict)

    try:
        max_id = resp.json()["max_id"]
        if max_id:
            return max_id
        else:
            return
    except:
        return


def get_all_data(params):
    """
    :param params: get请求需要的参数，数据类型为字典
    :return:
    """
    max_id = get_one_page(params)
    params["max_id"] = max_id
    params["count"] = 20
    while max_id:
        time.sleep(1)
        params["max_id"] = max_id
        max_id = get_one_page(params)
        if comment_number >= 80: break


if __name__ == '__main__':
    # 微博url
    weibo_url_list = [
        "https://weibo.com/2803301701/O7XXBzjyp?refer_flag=1001030103_"
    ]


    for weibo_url in weibo_url_list:
        comment_number = 0

        url_str = '.*?com\/\d+\/(.*)\?refer_flag=\d+_'
        res = re.findall(url_str, weibo_url)

        weibo_id = res[0]
        weibo_uid = weibo_url.split('/')[3]

        # csv写入表头
        # 拓展内容
        # "用户名称", "性别", "粉丝数量", "评论时间", "IP属地", "点赞数量",
        header = ["评论内容"]
        f = open("files/data.csv", "w", encoding="utf-8", newline="")
        writer = csv.DictWriter(f, header)
        writer.writeheader()

        headers = {
            'cookie': 'UOR=www.baidu.com,weibo.com,www.baidu.com; SINAGLOBAL=7684884535237.347.1706670996532; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5wH_9DUP1R3Ue.-nm11R2a5JpX5KMhUgL.Fo-RSo-fSh2fSKM2dJLoIEnLxK-L1KBLB-qLxKqL1hnL1K8ki--NiKyFi-8hi--fi-z7iKyWTCX_; XSRF-TOKEN=j3gFRIoKPJe17F85EhxHsbhR; ALF=1714663031; SUB=_2A25LCFEnDeRhGeNG7VcU9C_JzjuIHXVoZOzvrDV8PUJbkNANLVnXkW1NSyH8RFsA0_xotx4w27Wz4UOQJwbPc4e1; _s_tentry=weibo.com; Apache=5216999053811.295.1712071112489; ULV=1712071112490:6:1:1:5216999053811.295.1712071112489:1710079753861; WBPSESS=g4l_2WxUh8KH0JDRz93mbKIi-naQlPPka1Zipn1NSV3eF3Rz_GzOfe3JCGLfsrHP_cRQhAITUfzQCm19LFxhSkgbQDsPoVcZhd4jj-mHid1BU3t0qqVRXGPM5acyArqK4WZn_SxIwoljXtsr8dePDA==',
            'referer': "https://weibo.com/{}/{}".format(weibo_uid, weibo_id),
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            "x-xsrf-token": "oNLem1BqWdhFyx0jXjs7Syoa"
        }

        id = getArticleId(weibo_id)

        # get请求的参数
        # flow：0 按热度排序，flow：1 按时间排序
        params = {
            "flow": 1,
            "is_reload": 1,
            "id": id,
            "is_show_bulletin": 2,
            "is_mix": 0,
            "count": 10,
            "uid": weibo_uid
        }

        get_all_data(params)
        f.close()
        print("评论爬取完成")