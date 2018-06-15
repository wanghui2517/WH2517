from bs4 import BeautifulSoup
import html5lib
html_doc = """
<html>
    <head>
        <title>demo</title>
    </head>
<body>
    <table>
        <tr>
            <td class="ball_red">20</td>
        </tr>
        <tr>
            <td class="f_red">22</td>
        </tr>
        <tr>
            <td class="blue_red">23</td>
        </tr>
        <tr>
            <td class="ball_red">2</td>
        </tr>
        <tr>
            <td class="ball_red">11</td>
        </tr>
        <tr>
            <td class="ball_red">7</td>
        </tr>
        <tr>
            <td class="ball_red">14</td>
        </tr>
        <tr>
            <td class="ball_red">31</td>
        </tr>
    </table>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html5lib')
for tds in soup.find_all(name='td',attrs={'class':"ball_red"}):
    print(tds.contents)  
# print(soup.title)
# print(soup.body)
# print(soup.tr)
# #soup.find_all('tr')
# print(soup.find_all('tr'))
