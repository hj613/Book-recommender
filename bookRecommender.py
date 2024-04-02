# 오늘의 선택 페이지를 크롤링하여 책 리스트를 만드는 함수
# name: 도서명,  writer: 저자명, data_id = 책 고유번호
def create_bList(name, writer, data_id):
    pass

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