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






# 房天下爬虫作业

import requests
import time
import re
import os

# 1. 配置请求头与URL
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0"
}
urls = [f'https://suzhou.newhouse.fang.com/house/s/gongyeyuanqu/b9{i}' for i in range(1, 4)]

# ================== 网页本地化（已执行过，现注释） ==================
# for i, url in enumerate(urls, start=1):
#     print(f"正在下载第 {i} 页，URL: {url}")
#     try:
#         response = requests.get(url, headers=headers, timeout=5)
#         print(f"状态码: {response.status_code}")
#         response.encoding = 'utf-8'
#         filename = f"fang_page{i}.html"
#         with open(filename, "w", encoding="utf-8") as f:
#             f.write(response.text)
#         print(f"✅ {filename} 保存成功！")
#     except Exception as e:
#         print(f"❌ 第 {i} 页下载失败，错误原因: {e}")
#     time.sleep(10)
# print("循环结束！")

# ================== 解析本地文件 ==================

# 2. 获取绝对路径
base_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(base_dir, "suzhou_newhouse.txt")

# 3. 优化 I/O：打开文件放在外层，只开一次
with open(output_file, "w", encoding="utf-8") as f:
    # 4. 循环处理 1 到 3 页
    for i in range(1, 4):
        print(f"\n===== 正在解析第 {i} 页 =====")

        # 动态拼接本地 HTML 文件名
        filename = os.path.join(base_dir, f"fang_page{i}.html")

        # 容错：如果缺失某一页，跳过继续下一页
        try:
            with open(filename, "r", encoding="utf-8") as page_file:
                html = page_file.read()
        except FileNotFoundError:
            print(f"❌ 找不到 {filename}，请确认文件是否在 code 文件夹下！")
            continue

        # 5. 按每一个楼盘的外层标签切块
        li_list = re.findall(r'<li id="lp_\d+".*?</li>', html, re.S)
        print(f"本页找到 {len(li_list)} 个楼盘")

        # 6. 写入分页标题
        f.write(f"\n========== 第 {i} 页 ==========\n")

        # 7. 在每个楼盘内部单独提取名字和价格
        for li in li_list:
            # 提取楼盘名称
            name_m = re.search(r'class="nlcd_name".*?<a[^>]*>(.*?)</a>', li, re.S)
            name = name_m.group(1).strip() if name_m else "未知楼盘"

            # 提取价格区域，去掉 HTML 标签，只留纯文字
            price_m = re.search(r'<div class="nhouse_price">(.*?)</div>', li, re.S)
            if price_m:
                price = re.sub(r'<[^>]+>', '', price_m.group(1)).strip()
            else:
                price = "价格待定"

            print(f"楼盘：{name}\t价格：{price}")

            # 8. 直接写入文件（不用再 open 了）
            f.write(f"{name}\t{price}\n")

# 循环结束，文件自动关闭
print(f"\n🎉 全部解析完成！结果已保存到：{output_file}")
