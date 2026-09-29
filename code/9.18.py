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
import re
import os

headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0"}
urls=[f'https://suzhou.newhouse.fang.com/house/s/gongyeyuanqu/b9{i}'for i in range (1,4)]

print(urls)
# response = requests.get("https://suzhou.newhouse.fang.com/house/s/gongyeyuanqu/b91/", headers=headers)
# print(response.status_code)
# print(response.text[:1000])
# #
# url = "https://suzhou.newhouse.fang.com/house/s/gongyeyuanqu/b91"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }
#
# print("正在请求网页...")
# response = requests.get(url, headers=headers)
# response.encoding = 'utf-8'

