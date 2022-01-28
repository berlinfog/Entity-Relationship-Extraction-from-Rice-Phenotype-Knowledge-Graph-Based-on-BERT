"""
将字典对象保存为Json文件
"""

import os
import json


class SaveJson(object):

    def save_file(self, path, item):
        
        # 先将字典对象转化为可写入文本的字符串
        item = json.dumps(item)

        try:
            if not os.path.exists(path):
                with open(path, "w", encoding='utf-8') as f:
                    f.write(item + ",\n")
                    print("^_^ write success")
            else:
                with open(path, "a", encoding='utf-8') as f:
                    f.write(item + ",\n")
                    print("^_^ write success")
        except Exception as e:
            print("write error==>", e)


if __name__ == '__main__':
    # 保存的文件名
    path = "test1.json"
    # 案例字典数据
    item = {"uid": "5bc05421vbjgj34hj9c7d83", "oss_status_code": 200,
            "url": "https://ssyerv2.oss-cn-hangzhou.aliyuncs.com//picture/zl/687122.jpg",
            "updatedAt": "1970-01-18", "createdAt": "1970-01-18", "PID": "5b923c7vbcvbxcswrw342504b",
            "_id": "5b98d052ed0cbe41","CID":"afdsfgasgfafghdgssdhh"}

    s = SaveJson()

    # 测试代码，循环写入三行，没有空行
    for i in range(3):
        s.save_file(path, item)
