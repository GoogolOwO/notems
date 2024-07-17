# 引入selenium库中的 webdriver 模块
from selenium import webdriver
print("Note.ms 批量写入内容工具")
print("请勿用于批量打广告等操作，note.ms 没有规则。但因为违法对此带来的一切后果本工具开发者概不负责！请确保您已安装Chrome且为最新版本，driver.exe在同一目录下")
page = input("请输入想要显示的页面，请确保没有文本！（示例：如欲在note.ms/test显示，请输入test\n")
text = input("请输入想要显示的文本（换行请写\\n）\n")
times = int(input("请输入次数"))
print("即将开始，请勿关闭打开的浏览器窗口")
# 打开谷歌浏览器
driver = webdriver.Chrome()
# 打开百度搜索主页
driver.get('https://note.ms/' + page)
while times > 0:
    driver.find_element_by_xpath('/html/body/div/div[1]/div/div/textarea').send_keys(text)
    times = times - 1
driver.quit()
print("写入成功，请查看网址！")
print("Proudly made by Newtea EC")
input (":D")
