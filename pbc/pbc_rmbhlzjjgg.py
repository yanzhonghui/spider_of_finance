import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

# 人民币汇率中间价公告
options = Options()
options.add_argument('--headless')
driver = Chrome(executable_path='../chromedriver.exe', options=options)

try:
    driver.get('http://www.pbc.gov.cn/zhengcehuobisi/125207/125217/125925/index.html')
    totalpage = driver.find_element_by_id("r_con").find_element_by_tag_name('input').get_attribute('totalpage')
    page = int(totalpage)

    for p in range(1, page + 1):
        driver.get('http://www.pbc.gov.cn/zhengcehuobisi/125207/125217/125925/17105/index' + str(p) + '.html')
        table_tag = \
            driver.find_element_by_id("r_con").find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')[
                1].find_element_by_tag_name('td').find_elements_by_tag_name('table')
        for t in table_tag:
            a_tag = t.find_element_by_tag_name('a')
            span_tag = t.find_element_by_tag_name('span')
            a_tag_href = t.find_element_by_tag_name('a').get_attribute('href')
            print(a_tag.text + '\u0020' + span_tag.text + '：' + a_tag_href)
        time.sleep(2)

    driver.quit()
except:
    driver.quit()
