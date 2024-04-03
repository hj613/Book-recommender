# type
from . import bookRecommender

def saveFile(book : bookRecommender.RecommendBook, inputGenre):
    title = book.get_name()
    writer = book.get_writer()
    body = book.get_bInfo()
    url = book.get_url()
    
    with open(title + '.txt', 'w', encoding='UTF-8') as f:
        f.writelines(f"""
======>>>당신을 위한 오늘의 책<<<======

{inputGenre} 장르를 선택한 당신!
어떤 책을 읽을지 고민하고 있다면, 오늘은 이 책을 읽어보는 건 어떨까요?

========================================
# 도서명: {title}
# 저자: {writer}

# 책 소개
{body}

# 책 링크: {url}
========================================

오늘 당신의 독서 지수는 맑음!

잊지말고, 꼭!
출퇴근길, 점심 시간, 자기 전
잠깐의 시간을 내어 오늘의 책을 읽어 보세요!
                         """)