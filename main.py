from bookRecommender import getBook
from bookEmail import sendEmail

# init variables
enumGenre = {'소설': '01', '시/에세이': '03', '인문':'05','가정/육아':'07','요리':'08','건강':'09','취미/실용/스포츠':'11', '경제/경영':'13', '자기계발':'15', '정치/사회':'17', '역사/문화':'23', '종교':'21','예술/대중문화':'23','중/고등참고서':'25', '기술/공학': '26', '외국어':'27','과학':'29', '취업/수험서':'31', '여행':'32', '컴퓨터/IT':'33', '잡지':'35', '청소년':'38', '초등참고서':'39', '유아(0~7세)': '41', '어린이(초등)': '42', '만화': '47', '대학교재': '50', '한국소개도서': '53', '교보오리지널':'59'}

# intro
print('--------------------------')
print(r"Today's Book RECOMMENDER")
print('--------------------------')
print([g for g in enumGenre.keys()])

# input
inputGenre = input('위의 장르 중 원하시는 책 장르를 입력하세요. (예. 시/에세이) : ')
print('당신을 위한 책을 고르는 중입니다! 조금만 기다려주세요~')

# processing - get book
try :
    genre = enumGenre[inputGenre] # try-exception
except Exception:
    print('존재하지 않거나 올바르지 않은 입력했습니다. 다시 실행해주세요')
    exit()

book = getBook(genre)
print('책 선택 완료!')

# input
way = input('오늘의 책을 어떻게 받으시겠어요? 메일 / 파일 : ')

match way:
    case '메일':
        # processing - send email
        to_addr = input("이메일 : ")
        sendEmail(to_addr, book)
        
    case '파일':
        # processing - save file
        pass