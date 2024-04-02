# 필요한 모듈 import
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import time

# 오늘의 선택 페이지를 크롤링하여 책 리스트를 만드는 함수
# gerne : 입력 받은 장르명
def create_bList(gerne):
    # 기간 필터링을 위한 시간 변수 설정(today: 오늘 날짜, year_ago: 1년 전 날짜)
    today = datetime.today()
    year_ago = datetime.now() - timedelta(days=365)
    
    year_list = [datetime.year(), datetime.year() - 1]
    for year in year_list:
        # 2024, 2023 순서대로 페이지 열기
        url = 'https://product.kyobobook.co.kr/today-book/KOR/{gerne}#?sort=rec&year={year}&month=00'
        driver = webdriver.Chrome()
        driver.get(url)
        
        # 페이지 번호 가져오기
        pNumbers = driver.find_elements(By.CSS_SELECTOR, '#top_pagi > div > a')
        # 책 정보 리스트 가져오기
        bookList = []
        for p in pNumbers:
            bookData = driver.find_elements(By.CSS_SELECTOR, '#contents > div.switch_prod_wrap.view_type_list > ul')
            for book in bookData:
                liTag = book.find_elements(By.CSS_SELECTOR, 'li')
                for li in liTag:
                    # 책 추천일자 정보 가져오기
                    sDate = li.find_element(By.CSS_SELECTOR, 'div.prod_header > span > label').text
                    split_date = sDate.split('.')
                    bDate = datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))
                    # 현 시점에서 1년 이내 추천일자 책인지 확인 후 책 정보 가져오기(이름, 저자, 책 고유번호)
                    if (bDate >= year_ago) & (bDate <= today):
                        bName = li.find_element(By.CSS_SELECTOR, 'div.prod_area.horizontal > div.prod_info_box > div.auto_overflow_wrap.prod_name_group > div > div > a > span').text
                        bWriter = li.find_element(By.CSS_SELECTOR, 'div.prod_area.horizontal > div.prod_info_box > span > a').text
                        dataId = li.get_attribute('data-id')
                        bookList.append(Book(bName, bWriter, dataId))
            # 페이지 이동
            if (p.get_attribute('title') != '현재페이지') & (p.get_attribute('class') == 'btn_page_num'):
                p.click()
                time.sleep(5)
    # 책 리스트 반환
    return bookList

# 오늘의 선택 책 리스트 중 추천할 1권 책을 정하는 함수
# book_list: 책 리스트
def choose_book(book_list):
    pass

# 추천할 1권의 책의 상세 정보를 받아오는 함수
# data_id: 책 고유번호
def get_bInfo(data_id):
    pass

# 기본 책 class
# name: 도서명, writer: 저자명, data_id: 책 고유번호
class Book:
    def __init__(self, name, writer, data_id):
        self.__name = name
        self.__writer = writer
        self.__id = data_id

# 추천 책 class(Book class 상속)
# info: 책 상세 정보, image: 책 표지 img src
class RecommendBook(Book):
    def __init__(self, info, image):
        super().__init__
        self.__info = info
        self.__image = image