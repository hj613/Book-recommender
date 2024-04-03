from bookRecommender import getBook
from bookEmail import sendEmail
from bookFile import saveFile

# init variables
enumGenre = {'소설': '01', '시': '03', '에세이': '03', '시/에세이': '03', '인문':'05','가정':'07', '육아': '07', '가정/육아': '07',
             '요리':'08','건강':'09','취미': '11', '실용': '11', '스포츠':'11', '취미/실용/스포츠':'11', '경제': '13', '경영':'13',
             '경제/경영': '13', '자기계발':'15', '정치': '17', '사회': '17','정치/사회':'17', '역사': '23', '문화': '23', '역사/문화':'23',
             '종교':'21', '예술': '23', '대중문화': '23', '예술/대중문화':'23', '중/고등참고서':'25', '기술': '26', '공학': '26',
             '기술/공학': '26', '외국어':'27','과학':'29', '취업/수험서':'31', '여행':'32', '컴퓨터': '33', 'IT': '33', '컴퓨터/IT':'33',
             '잡지':'35', '청소년':'38', '초등참고서':'39', '유아(0~7세)': '41', '어린이(초등)': '42', '만화': '47', '대학교재': '50', '한국소개도서': '53', '교보오리지널':'59'}

# intro
print('--------------------------')
print(r"Today's Book RECOMMENDER")
print('--------------------------')
print('''
|   소설  |  시/에세이  |  인문  |  가정/육아  |  요리  |  건강  |
|   취미/실용/ 스포츠  |  경제/경영  |  자기계발  |  정치/사회   |
|   역사/문화  |   종교   |   예술/대중문화   |   중/고등참고서  |
|   기술/공학   |  외국어  |   과학   |  취업/수험서  |   여행   |
|   컴퓨터/IT   |  잡지  |  청소년  |  초등참고서  | 유아(0~7세) |
|   어린이(초등) | 만화 | 대학교재 | 한국소개도서 | 교보오리지널 |      
      ''')

# input
inputGenre = input('위의 장르 중 원하시는 책 장르를 입력하세요. : ')
print('--------------------------')

print('당신을 위한 책을 고르는 중입니다...')
print('조금만 기다려 주세요!')

# processing - get book
try :
    genre = enumGenre[inputGenre] # try-exception
except Exception:
    print('존재하지 않거나 올바르지 않은 입력했습니다. 다시 실행해주세요.')
    exit()

book = getBook(genre)
print('두근두근... 책 선택 완료!')
print('--------------------------')

# input
try :
    way = input('오늘의 책을 어떻게 받으시겠어요? 메일 / 파일 : ')
    if way == '':
        raise ValueError()
except ValueError:
    print('입력하지 않았습니다. 다시 실행해주세요.')
    exit()

# save or send
try :
    match way:
        case '메일':
            # send email
            to_addr = input("이메일 : ")
            sendEmail(to_addr, book)
        case '파일':
            # save file
            saveFile(book, inputGenre)
except Exception as e:
    print("에러가 발생했습니다")
    print(e)