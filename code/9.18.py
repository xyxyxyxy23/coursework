# 统计系名单提取

# import re
#
# html_text = '''
# <td style="padding: 5px 10px; border: 1px solid rgb(51, 51, 51); border-image: none;">统计系</td>
# <td style="padding: 5px 10px; border: 1px solid rgb(51, 51, 51); word-break: break-all;">王开永 董迎辉</td>
# <td style="padding: 5px 10px; border: 1px solid rgb(51, 51, 51); word-break: break-all;">梁 雪</td>
# <td style="padding: 5px 10px; border: 1px solid rgb(51, 51, 51); word-break: break-all;">张 妍 李秋芳 周 莉<br>吕高凤 郭 洁 李 龙<br>朱笑雨 付文豪 周从金<br>陈 锷</td>
# '''
#
# names0=re.sub(r'<br>',' ',html_text)#换行标签变为空格
# names1=re.sub(r'<td.*?>','',names0)#所有 <td style="..."> 都没了，只剩内容和 </td>。
# names2=re.sub(r'</td>','',names1)#只剩纯文字
# names3=re.sub(r'\s+',' ',names2)#\s+ 匹配"一个或多个空白"（空格、换行、制表符） 只剩一行纯文字
# names4=re.sub(r'统计系','',names3)
#
# words=names4.split()#按任意空白（空格、换行、制表符）切分
# print('words is:',words)
# #
# names=[]
# i=0
# while i<len(words):
#     if len(words[i])==1:
#         names.append(words[i]+words[i+1])
#         i=i+2
#     else:
#         names.append(words[i])
#         i=i+1
# print(names)



# names = re.findall(r'[\u4e00-\u9fa5]\s?[\u4e00-\u9fa5](?:\s?[\u4e00-\u9fa5])?', html_text)
# names = [n.replace(' ', '') for n in names]
# names = [n for n in git config --global user.email "xyxyxyxy23@users.noreply.github.com"names if n != '统计系']
#
#print(names3)






#房天下
import requests
import time

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0"
}
urls = [f'https://suzhou.newhouse.fang.com/house/s/gongyeyuanqu/b9{i}' for i in range(1, 4)]

# for i, url in enumerate(urls, start=1):
#     # 先打印出这次请求的URL，看看对不对
#     print(f"正在下载第 {i} 页，URL: {url}")
#
#     try:
#         # 加入 timeout=5，防止网络卡死一直等
#         response = requests.get(url, headers=headers, timeout=5)
#
#         # 打印状态码，正常应该是 200
#         print(f"状态码: {response.status_code}")
#
#         response.encoding = 'utf-8'
#         filename = f"fang_page{i}.html"
#         with open(filename, "w", encoding="utf-8") as f:
#             f.write(response.text)
#         print(f"✅ {filename} 保存成功！")
#
#     except Exception as e:
#         # 如果报错，直接打印出具体的错误原因
#         print(f"❌ 第 {i} 页下载失败，错误原因: {e}")
#
#     # 休息两秒防封
#     time.sleep(10)
#
# print("循环结束！")

import re
import os

# 获取当前文件夹路径（防止找不到文件）
base_dir = os.path.dirname(os.path.abspath(__file__))

# 直接循环3次，解析3个本地文件
import re
import os

# 1. 获取当前代码所在的文件夹路径
base_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(base_dir, "suzhou_newhouse.txt")

# 2. 每次运行前，先清空旧的 txt 文件（防止数据无限叠加）
with open(output_file, "w", encoding="utf-8") as f:
    pass

# 3. 循环处理第 1 到 3 页
for i in range(1, 4):
    print(f"\n===== 正在解析第 {i} 页 =====")

    # 动态拼接本地 HTML 文件名
    filename = os.path.join(base_dir, f"fang_page{i}.html")

    try:
        # 读取本地 HTML 文件
        with open(filename, "r", encoding="utf-8") as f:
            html = f.read()
    except FileNotFoundError:
        print(f"❌ 找不到 {filename}，请确认文件是否在 code 文件夹下！")
        continue

    # 4. 按每一个楼盘的外层标签切块
    li_list = re.findall(r'<li id="lp_\d+".*?</li>', html, re.S)
    print(f"本页找到 {len(li_list)} 个楼盘")

    # 5. 每次开始写这一页数据前，先往 txt 里写个分页标题
    with open(output_file, "a", encoding="utf-8") as f:
        f.write(f"\n========== 第 {i} 页 ==========\n")

    # 6. 在每个楼盘内部单独提取名字和价格
    for li in li_list:
        # 提取楼盘名称
        name_m = re.search(r'class="nlcd_name".*?<a[^>]*>(.*?)</a>', li, re.S)
        name = name_m.group(1).strip() if name_m else "未知楼盘"

        # 提取价格区域，去掉 HTML 标签，只留纯文字（不管均价还是总价，原样保存）
        price_m = re.search(r'<div class="nhouse_price">(.*?)</div>', li, re.S)
        if price_m:
            # 利用正则去掉 <span> 等多余标签，并去掉前后空格
            price = re.sub(r'<[^>]+>', '', price_m.group(1)).strip()
        else:
            price = "价格待定"

        print(f"楼盘：{name}\t价格：{price}")

        # 7. 追加写入到 txt 文件
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(f"{name}\t{price}\n")

print(f"\n🎉 全部解析完成！结果已保存到：{output_file}")
