# 🧲 당근마켓 중고 물품 크롤러

키워드와 지역을 기준으로 당근마켓의 중고 물품 정보를 수집하는 Python 크롤러입니다.  
빠르게 원하는 정보만 추려보고 싶은 분들을 위한 미니 자동화 도구예요.

---

## 🛠 사용 기술 및 라이브러리

| 카테고리 | 라이브러리 | 설명 |
|----------|------------|------|
| GUI      | `tkinter`, `ttk`, `PIL.ImageTk` | 데스크탑 사용자 인터페이스 및 이미지 렌더링 |
| 크롤링   | `requests`, `BeautifulSoup`, `urllib.parse` | 웹 페이지 요청 및 HTML 파싱 |
| 비동기   | `asyncio`, `aiohttp`, `concurrent.futures`, `ThreadPoolExecutor`, `threading` | 동시성 처리 및 성능 향상 |
| 데이터 처리 | `json`, `base64`, `datetime`, `time`, `queue`, `functools.lru_cache` | 다양한 데이터 처리 및 캐싱 |
| 보안     | `cryptography.Fernet` | 민감한 정보 암호화 |
| 기타     | `os`, `sys`, `io.BytesIO` | 파일/시스템 입출력 등 기본 유틸리티 |

---

## 🚀 사용 방법

```bash
git clone https://github.com/your-username/daangn-crawler.git
cd daangn-crawler
pip install -r requirements.txt
python crawler.py
```

> ⚠ 지역/키워드는 코드 내에서 직접 설정하실 수 있어요.

---

## 💡 주요 기능

- 키워드 기반 중고 물품 검색
- 지역 필터링 기능
- 제목, 가격, 위치, 상세 링크 수집
- CSV로 저장 가능 (데이터 가공 용이)

---

## 📸 예시 출력

| 제목             | 가격       | 지역         | 링크                     |
|------------------|------------|--------------|--------------------------|
| 나이키 운동화 팝니다 | 70,000원  | 서울 강남구   | [보러가기](https://daangn.net/...) |

---

## 🔒 주의사항

- 크롤링은 사이트의 정책에 따라 제한될 수 있습니다.
- 비정상적으로 빠른 요청은 차단의 원인이 될 수 있으니, `time.sleep()`을 적절히 넣어주세요.
- 상업적 용도보다는 개인 학습/포트폴리오용 활용을 권장드립니다.

---

## 🙋🏻‍♂️ 만든 사람

- **이름**: 홍길동  
- **연락처**: hong@example.com  
- **포트폴리오**: [hongdev.tistory.com](https://hongdev.tistory.com)

---

> 👀 사용 중 이슈나 피드백이 있다면 언제든지 PR 또는 이슈 등록 부탁드립니다!
