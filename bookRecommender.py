# 필요한 모듈 import
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import time

# 오늘의 선택 페이지를 크롤링하여 책 리스트를 만드는 함수
# name: 도서명,  writer: 저자명, data_id = 책 고유번호
def getYearsBetweenOne():
    today = datetime.today()
    year_ago = datetime.now() - timedelta(days=365)

    return [today, year_ago]

def isWithinYear(element, years):
    split_date = element.split('.')
    bDate = datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    if (bDate >= years[1]) & (bDate <= years[0]):
        return True
    else:
        return False

def create_bList(genre):
    driver = webdriver.Chrome()
    bookList = []
    for year in getYearsBetweenOne(): # [2024, 2023]
        # url
        url = f'https://product.kyobobook.co.kr/today-book/KOR/{genre}#?sort=rec&year={year.year}&month=00'
        driver.get(url)
        time.sleep(5)

        # get the page numbers
        pageList = [a for a in driver.find_elements(By.CSS_SELECTOR, '#top_pagi > div > a') if not a.get_attribute('class').endswith("hidden")]
        
        # processing
        for p in pageList:
            # move page
            if (p.get_attribute('title') != '현재페이지') & (p.get_attribute('class') == 'btn_page_num'):
                p.click()
                time.sleep(5)
            
            # get book information list
            bookData = driver.find_elements(By.CSS_SELECTOR, '#contents > div.switch_prod_wrap.view_type_list > ul > li')
            for book in bookData:
                if isWithinYear(book.find_element(By.CSS_SELECTOR, 'div.prod_header > span > label').text, getYearsBetweenOne()):
                    bName = book.find_element(By.CSS_SELECTOR, 'div.prod_area.horizontal > div.prod_info_box > div.auto_overflow_wrap.prod_name_group > div > div > a > span').text
                    bWriter = book.find_element(By.CSS_SELECTOR, 'div.prod_area.horizontal > div.prod_info_box > span > a').text
                    dataId = book.get_attribute('data-id')
                    bookList.append(Book(bName, bWriter, dataId))
                    
    # finally
    return bookList

# 오늘의 선택 책 리스트 중 추천할 1권 책을 정하는 함수
# book_list: 책 리스트
def choose_book(book_list):
    return book_list[random.randint(0, len(book_list))] 

# 추천할 1권의 책의 상세 정보를 받아오는 함수
# chosen_book : 위에서 선택된 1권의 Book class
def get_bInfo(chosen_book):
    book_id = chosen_book.get_id()
    
    # 책 상세 페이지 열기
    driver = webdriver.Chrome()
    url = f'https://product.kyobobook.co.kr/detail/{book_id}'
    driver.get(url)
    
    # 책 표지 img src 저장
    imgTag = driver.find_element(By.CSS_SELECTOR, '#contents > div.prod_detail_header > div > div.prod_detail_view_wrap > div > div.col_prod_info.thumb > div.prod_thumb_swiper_wrap.active > div.swiper-container.prod_thumb_list_wrap.swiper-container-fade.swiper-container-horizontal > ul > li.prod_thumb_item.swiper-slide.swiper-slide-visible.swiper-slide-active > div > div.portrait_img_box.portrait > img')
    image = imgTag.get_attribute('src')
    
    # 책 소개 내용 저장
    bInfo = driver.find_element(By.CSS_SELECTOR, '#scrollSpyProdInfo > div.product_detail_area.book_intro > div.intro_bottom').text
    
    # 저자 소개 내용 저장
    wInfo = driver.find_element(By.CSS_SELECTOR, '#scrollSpyProdInfo > div.product_detail_area.product_person > div.round_gray_box > div.writer_info_box > div > div.auto_overflow_contents > div > p').text
    
    today_book = RecommendBook(chosen_book, bInfo, wInfo, image)
    return today_book

# 기본 책 class
# name: 도서명, writer: 저자명, data_id: 책 고유번호
class Book:
    def __init__(self, name, writer, data_id):
        self.__name = name
        self.__writer = writer
        self.__id = data_id
    
    def get_name(self):
        return self.__name
    
    def get_writer(self):
        return self.__writer
        
    def get_id(self):
        return self.__id
        
    def __str__(self):
        return f'도서명: {self.__name}, 저자: {self.__writer}'

# 추천 책 class(Book class 상속)
# bInfo: 책 상세 정보, wInfo: 저자 상세 정보, image: 책 표지 img src
class RecommendBook(Book):
    def __init__(self, book, bInfo, wInfo, image):
        super().__init__(book.get_name(), book.get_writer(), book.get_id())
        self.__bInfo = bInfo
        self.__wInfo = wInfo
        self.__image = image
        
    def get_wInfo(self):
        return self.__wInfo
    
    def get_bInfo(self):
        return self.__bInfo
    
    def get_image(self):
        return self.__image
        
    def __str__(self):
        return super().__str__() + f'저자 정보: {self.__wInfo}\n책 소개:\n{self.__bInfo}'

# finally
def getBook(genre):
    return get_bInfo(choose_book(create_bList(genre)))