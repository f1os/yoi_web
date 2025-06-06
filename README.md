# 요구사항
Python
- Python 3.12
---

## 실행
### 필수 패키지 설치
```
pip install -r requirements.txt
```

### 마이그레이션
```
python manage.py migrate
```

### 초기 데이터 로드
```
python manage.py loaddata posts.json
```

### 애플리케이션 실행
```
python manage.py runserver 8000
```

### 접속
http://localhost:8000
