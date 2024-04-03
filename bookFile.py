# type
from bookRecommender import RecommendBook

def saveFile(filename, book: RecommendBook):
    title = book.get_name()
    writer = book.get_writer()
    body = book.get_bInfo()
    url = book.get_url()
    
    with open(filename + '.txt', 'w', encoding='UTF-8') as f:
        f.writelines(f"""제목: 책 추천
안녕하세요!

제가 추천하는 책 정보입니다.

===================================
책 제목: {title}
저자: {writer}

책 소개:
{body}

책 링크: {url}
===================================

이 책을 읽어보시면 좋을 것 같습니다. 궁금한 점이 있다면 언제든 연락주세요.

감사합니다.""")