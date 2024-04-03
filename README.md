# Today's Book Recommender

교보문고 오늘의 선택 사이트에서 책 목록을 추출한 다음 랜덤으로 1권을 골라 메일 보내거나 파일 저장하는 프로그램입니다.

## 목차

- [설치 방법](#설치-방법)
- [사용 방법](#사용-방법)
- [파일 설명](#파일-설명)

### 설치 방법 ⚙️

1. 이 저장소를 클론하거나 ZIP 파일로 다운로드합니다.

### 사용 방법 ⭐

1. `main.py` 파일을 실행합니다.
2. 읽고 싶은 장르를 입력합니다. 
3. 프로그램이 교보문고 웹 사이트에서 책 정보를 크롤링합니다.
4. 크롤링된 책 목록 중 한 권의 책이 추천됩니다.
5. 추천된 책의 제목, 작가, 설명 등의 정보를 이메일 전송 또는 파일 저장하는 방법을 고릅니다.
6. 정보를 확인할 수 있습니다.

### 파일 설명 🗒️

- `main.py` 프로그램의 주요 실행 파일입니다. 기본적인 Input 동작하며 기능들을 호출하는 파일입니다.
- `bookEmail.py` 이메일 전송 모듈입니다.
- `bookFile.py` 파일 저장 모듈입니다.
- `bookRecommender.py` 교보문고 웹 사이트에서 책 정보를 크롤링하는 모듈입니다.

## ❤️

### 역할 분담

hj613 - Site Crawling / File Output  
gntodtndls156 - Saving File & Sending Email System

### 프로젝트 환경

SNS - Slack  
Git - Issue, Project  
Tool - VS CODE  
Program - Python, Selenium