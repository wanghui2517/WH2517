from bs4 import BeautifulSoup

# with open('test.html','r+',encoding = 'utf-8') as f:
#     demo = f.readlines()
soup = BeautifulSoup(open('test.html',encoding = 'utf-8'),'html5lib')
#dataList = [{'period':'18067','red_ball':['1','2','3','4','5'],'blue_ball':['1','2']},{'period':'18066','red_ball':['1','2','3','4','5'],'blue_ball':['1','2']}]
dataList = []
# red_ball = []
# blue_ball = []
caipiao = {}
caipiao["period"] = ''
caipiao["red_ball"] = []
caipiao["blue_ball"] = []
attrs1 = {'height':23}
attrs2 = {'class':"red"}
attrs3 = {'class':"blue"}
# dic = {'period':'18067','red_ball':['1','2','3','4','5'],'blue_ball':['1','2']}
# print(dataList[1])
# print(dataList[1]['period'])
# for trs in soup.find_all(name='tr',attrs={'class':"data-period"}):
#     print(trs.contents)
# for tds in soup.find_all(name='td',attrs={'class':"ball_red"}):
#     print(tds.contents)
demo = soup.find('tbody')
# print(demo.prettify())
#失败一
# for trs in demo.find_all(name='td',attrs={'height':23}):
# #     #print(trs.contents)
# #     #print(period)
# #     #periodList.append(trs.contents)
# #     # print(periodList)
#     periodList.append(trs.contents[0].replace("/n","").strip())
#     print(periodList)
# print(len(periodList))
#失败二
# for trs in demo.find_all('tr'):
#     for tds in trs.find_all('td'):
        # if tds.attrs == {'height':23}:
        #     periodList.append(tds.content[0].replace("/n","").strip())
        # elif tds.attrs == {'class':'red'}:
        #     red_ball.append(tds.contents[0].replace("/n","").strip())
        # elif tds.attrs == {'class':'blue'}:
        #     blue_ball.append(tds.contents[0].replace("/n","").strip())
        # else:
        #     periodList = None
        #     red_ball = None
        #     blue_ball = None

        #print(periodList,blue_ball,red_ball)
        #print(tds.contents)
#失败三
# for trs in demo.find_all(name='td',attrs={'height':23}):
#     periodList.append(trs.contents[0].replace("/n","").strip())
#     for tds in trs.find_all(name='td',attrs=attrs2) or trs.find_all(name='td',attrs=attrs3):
#         if tds.attrs == attrs2:
#             red_ball.append(tds.contents[0].replace("/n","").strip())
#         elif tds.attrs == attrs3:
#             blue_ball.append(tds.contents[0].replace("/n","").strip())
#         print(periodList,red_ball,blue_ball)
#失败四
# for tds in demo.find_all(name='td',attrs=attrs2):
#     red_ball.append(tds.contents[0].replace("/n","").strip())
#     print(red_ball)
#     print(len(red_ball))
# for tds in demo.find_all(name='td',attrs=attrs3):
#     blue_ball.append(tds.contents[0].replace("/n","").strip())
#     print(blue_ball)
#     print(len(blue_ball))
# for tds in demo.td:
#     print(tds)
#print(demo.td)默认找到第一个td
#失败五
# for tds in demo.find_all(name='td',attrs=attrs1):
#     periodList.append({'period':tds.contents[0].replace("/n","").strip()})
#     for tds1 in tds.find_all(name='td',attrs=attrs2):
#         red_ball.append({'red_ball':[tds1.contents.replace("/n","").strip()]})
#         for tds2 in tds.find_all(name='td',attrs=attrs3):
#             blue_ball.append({'blue_ball':[tds2.contents.replace("/n","").strip()]})
#失败六
# print(periodList,red_ball,blue_ball)
# for tds in demo.find_all(name='td',attrs=attrs1):
#     for tds1 in tds.find_all(name='td',attrs=attrs2):
#         for tds2 in tds.find_all(name='td',attrs=attrs3):
#             periodList.append({'period':tds.contents[0].replace("/n","").strip()})
#             # periodList.append({'red_ball':[tds1.contents.replace("/n","").strip()]})
#             # periodList.append({'blue_ball':[tds2.contents.replace("/n","").strip()]})
# print(periodList)
#失败七
# for tds in demo.find_all(name='td',attrs=attrs1):
#     dataList.append(caipiao{["period"] = tds.contents[0].replace("/n","").strip()})
#     for tds1 in tds.find_all(name='td',attrs=attrs2):
#         #red_ball.append({'red_ball':[tds1.contents.replace("/n","").strip()]})
#         dataList.append(caipiao["red_ball"] = tds1.contents.replace("/n","").strip())
#         for tds2 in tds.find_all(name='td',attrs=attrs3):
#             #blue_ball.append({'blue_ball':[tds2.contents.replace("/n","").strip()]})
#             dataList.append(caipiao["blue_ball"] = tds2.contents.replace("/n","").strip())
# print(dataList)
