# city-voice-info

## 사용자의 음성을 듣고 해당 도시의 정보를 알려줍니다.

### 기능

- 음성 명령 듣기
- 명령에서 도시 이름 찾기
- 도시의 현재 날짜와 시간 알려주기
- 도시의 날씨와 온도 알려주기
- 종료라고 말하면 프로그램 종료

### 설치 방법

- git clone https://github.com/gomverse/city-voice-info.git
- cd city-voice-info

### 필요한 패키지 설치

- pip install -r requirements.txt
- 프로젝트 폴더에 .env 파일 생성 후 API 키 입력
- OPENWEATHER_API_KEY=여기에_발급받은_API_키를_입력하세요

### 사용 방법

- #### 명령 예시
- 서울의 시간과 날짜를 알려줘
- 뉴욕의 날씨를 알려줘
- 런던의 시간을 알려줘

### 파일 목록

- city-voice-info.py : 메인 코드
- requirements.txt : 필요한 패키지 목록
- .env : API 키 파일
