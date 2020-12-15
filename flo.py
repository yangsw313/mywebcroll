from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-fullscreen')
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
"""chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('lang =ko_KR')"""
driver = webdriver.Chrome(options=chrome_options)

move = ActionChains(driver)
user_id = 'yangsw313'
user_pw = 'jong7322!'
url = 'https://www.music-flo.com/'

search = input("노래 검색 및 재생 : ")
"""time.sleep(1)
driver.maximize_window()
time.sleep(2)"""

realsearch = f'{search}'

first_login = '//*[@id="header"]/div/div/ul/li[2]/a'  # 처음 로그인 버튼
tlogin_pop = '//*[@id="main"]/div/div/div[2]/a[1]'  # T아이디로 로그인
tlogin_id = '//*[@id="userId"]'  # T로그인 팝업창에서 아이디
tlogin_pw = '//*[@id="password"]'  # T로그인 팝업창에서 패스워드
tlogin_login = '//*[@id="authLogin"]'  # T 로그인 팝업창에서 로그인 버튼
driver.implicitly_wait(5)
print("FLO 들어가는중...")
driver.get(url)
driver.implicitly_wait(5)
login_btn = driver.find_element_by_xpath(first_login)
driver.implicitly_wait(5)  # flo 로그인 버튼 찾고 클릭
print("로그인 과정 진행중...")
login_btn.click()
driver.implicitly_wait(5)
print("T아이디로 로그인중..")
tlogin_btn = driver.find_element_by_xpath(tlogin_pop)  # t 아이디로 로그인 버튼 클릭
driver.implicitly_wait(5)
tlogin_btn.click()
driver.implicitly_wait(5)
print("팝업 스위치 중...")
last_tap = driver.window_handles[-1]
driver.switch_to.window(window_name=last_tap)  # t 로그인 창 팝업 스위치
driver.implicitly_wait(5)
tloginid_btn = driver.find_element_by_xpath(tlogin_id)  # t 아이디 클릭, 아이디 붙여넣기
driver.implicitly_wait(5)
tloginid_btn.click()
print("아이디 입력...")
driver.implicitly_wait(5)
pyperclip.copy(user_id)
driver.implicitly_wait(5)
tloginid_btn.send_keys(Keys.CONTROL, 'v')
print("아이디 입력 완료")
time.sleep(0.1)
driver.implicitly_wait(5)
tloginpw_btn = driver.find_element_by_xpath(tlogin_pw)  # t 패스워드 클릭, 패스워드 붙여넣기
print("패스워드 입력...")
driver.implicitly_wait(5)
tloginpw_btn.click()
pyperclip.copy(user_pw)
driver.implicitly_wait(5)
tloginpw_btn.send_keys(Keys.CONTROL, 'v')
time.sleep(0.1)
tloginlogin_btn = driver.find_element_by_xpath(tlogin_login)
driver.implicitly_wait(5)
tloginlogin_btn.click()
print("로그인 완료 !")
driver.implicitly_wait(5)
print(driver.window_handles)
print("팝업 재스위치 중...")
last_tap1 = driver.window_handles[0]
driver.switch_to.window(window_name=last_tap1)
driver.implicitly_wait(3)

# 키워드 검색
time.sleep(2)
print("'%s' 입력중.." % search)
driver.find_element_by_xpath('//*[@id="searchKeywordInput"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="searchKeywordInput"]').send_keys(realsearch)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="searchKeywordInput"]').send_keys(Keys.ENTER)
driver.implicitly_wait(3)
time.sleep(0.5)
print("PLAY")
driver.find_element_by_css_selector('.btn_thumbnail_play').click()  # 대표 곡 재생
# driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/table/tbody/tr[1]/td[4]/button').click() # 2번째 곡 버튼
driver.implicitly_wait(2)
time.sleep(1)
try:
    driver.find_element_by_css_selector('.popup_w common-alert')
    driver.find_element_by_xpath('//*[@id="btnAlert1"]').click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/section[1]/div/div[1]/div[1]').click() # 전체 화면으로 변환
    time.sleep(1)
    volumeslider = driver.find_element_by_xpath('//*[@id="app"]/div[3]/section[1]/div/div[2]/div[3]/div/div/input')
    time.sleep(5)
    move.click_and_hold(volumeslider).move_to_element_with_offset(volumeslider, 5, 0).perform()
except:
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/section[1]/div/div[1]/div[1]').click()  # 전체 화면으로 변환
    volumeslider = driver.find_element_by_xpath('//*[@id="app"]/div[3]/section[1]/div/div[2]/div[3]/div/div/input')
    time.sleep(5)
    move.click_and_hold(volumeslider).move_to_element_with_offset(volumeslider, 5, 0).perform()

# 볼륨 바




"""
    windowpop = driver.find_element_by_css_selector('.popup_w.common-alert')
    if windowpop.is_displayed():
        driver.find_element_by_css_selector('.btn_bg_white_s').click()
        print("성인인증 필요, 재생불가")
"""

'''
driver.find_element_by_css_selector('.forward.btn_paging_arrow.PERSONAL_btn_forward').click()
time.sleep(1)
driver.find_element_by_css_selector('.forward.btn_paging_arrow.PERSONAL_btn_forward').click()
time.sleep(2)
driver.find_element_by_css_selector('.forward.btn_paging_arrow.PERSONAL_btn_forward').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="main"]/div/section[1]/div[2]/ul/li[4]/button').click() # 재생 버튼 클릭
windowpopup = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div')
if windowpopup.is_displayed():
    driver.find_element_by_css_selector('.btn_bg_white_s').click()
'''
