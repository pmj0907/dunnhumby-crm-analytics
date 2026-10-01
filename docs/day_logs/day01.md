# Day 1 — 데이터 구조 이해 및 키 관계 검증

## 1. 오늘 완료한 것

- Python 3.14 기반 프로젝트 가상환경 `.venv` 생성
- `kagglehub`, `pandas` 설치 및 `requirements.txt` 생성
- KaggleHub로 dunnhumby 데이터 다운로드
- 전체 8개 CSV의 컬럼 구조 확인
- `inspect_schema.py`, `inspect_keys.py` 작성
- PK / FK / 복합키 후보 검증
- key 포함관계 및 중복 데이터 확인
- VS Code `# %%` 셀 방식 학습


## 2. 테이블 구조 정리

### hh_demographic
- Grain: 한 가구의 인구통계 정보
- PK 후보: `household_key`
- 거래 고객 2,500가구 중 demographic 정보가 있는 가구는 801개
- 전체 고객 마스터가 아니라 일부 household의 속성 테이블로 판단

### transaction_data
- Grain: 한 장바구니 안 특정 상품의 구매내역
- PK 후보: `(BASKET_ID, PRODUCT_ID)`
- FK 후보: `household_key`, `PRODUCT_ID`
- `PRODUCT_ID`는 product 테이블과 완전히 연결됨
- `household_key`는 demographic과 논리적으로 연결되지만 모든 값이 존재하지는 않음

### product
- Grain: 한 상품의 기본 정보
- PK 후보: `PRODUCT_ID`
- 총 92,353개 상품
- 거래에 등장한 상품은 92,339개
- 14개 상품은 거래 데이터에 등장하지 않음

### campaign_desc
- Grain: 한 캠페인의 기본 정보
- PK 후보: `CAMPAIGN`
- 30개 캠페인 모두 고유

### campaign_table
- Grain: 특정 household와 특정 campaign의 관계
- PK 후보: `(household_key, CAMPAIGN)`
- `CAMPAIGN` → `campaign_desc.CAMPAIGN`

### coupon
- `COUPON_UPC` 단독으로 유일하지 않음
- `(COUPON_UPC, PRODUCT_ID, CAMPAIGN)` 조합에서도 중복 존재
- 전체 컬럼 기준 완전 동일 행 5,164건 존재
- 데이터 품질 이슈로 판단

### coupon_redempt
- Grain: 특정 household가 특정 날짜에 특정 캠페인의 특정 쿠폰을 사용한 기록
- PK 후보: `(household_key, DAY, COUPON_UPC, CAMPAIGN)`
- `DAY`를 제외하면 30건 중복

### causal_data
- 초기 예상 grain: `(PRODUCT_ID, STORE_ID, WEEK_NO)`
- 해당 조합에서 15,245건 중복
- 실제 중복 사례 확인 결과 같은 상품·매장·주차에서도 `display` 값이 다를 수 있음
- 실제 물리적 grain 후보:
  `(PRODUCT_ID, STORE_ID, WEEK_NO, display, mailer)`


## 3. 새로 배운 개념

### PK
한 테이블에서 각 행을 유일하게 구분하는 키.

### FK
다른 테이블의 PK를 참조해 테이블 간 관계를 연결하는 키.

### 복합키
단일 컬럼으로 행을 구분할 수 없을 때 여러 컬럼을 함께 사용하는 키.

### Grain
테이블의 한 행이 실제로 무엇을 의미하는지 나타내는 데이터 단위.

### 참조 무결성
FK 값이 부모 테이블의 PK에 실제로 존재하는 상태.

### 논리적 관계
업무 의미상 서로 연결되지만 실제 데이터에서 모든 key가 존재하지 않을 수도 있는 관계.

### 차집합
단순한 고유값 개수 차이와 실제 key 포함관계는 다르므로 집합 비교가 필요함.


## 4. 주요 발견

### household 포함관계
- transaction에만 존재하는 household: 1,699개
- demographic에만 존재하는 household: 0개

따라서 demographic의 801가구는 모두 transaction에 포함되지만, demographic은 전체 거래 고객을 포함하지 않는다.

### product 포함관계
- transaction에만 존재하는 PRODUCT_ID: 0개
- product에만 존재하는 PRODUCT_ID: 14개

transaction의 모든 상품은 product 테이블에 존재한다.

### coupon 중복
전체 컬럼이 동일한 행이 5,164건 존재한다.

### causal_data grain
문서나 컬럼명만 보고 예상한 grain과 실제 데이터의 grain이 다를 수 있음을 확인했다.


## 5. 문제 해결

### KaggleHub 다운로드 오류
`data/raw` 폴더에 `.gitignore` 테스트용 `test.txt`가 남아 있어 다운로드가 실패했다.

파일을 삭제하고 다시 실행해 해결했다.

### Python 환경
pyenv-win 업데이트 과정에서 오류가 발생해 Windows Python Launcher의 Python 3.14를 직접 지정하여 `.venv`를 생성했다.

### causal_data 중복
예상한 key 조합에서 중복이 발견되어 실제 중복 행을 출력해 원인을 확인했다.


## 6. AI 활용

- Git / GitHub 및 Python 환경 개념 학습
- DB 키와 grain 개념 설명
- key 유일성 및 포함관계 검증 코드 작성
- 오류 원인 분석
- 데이터 구조에 대한 가설을 먼저 세운 뒤 실제 데이터로 검증하는 방식으로 활용


## 7. 직무 관점에서 느낀 점

고객 분석에서는 지표 계산이나 모델링 이전에 데이터 구조와 분석 모집단을 정확히 이해하는 과정이 중요하다.

특히 어떤 테이블을 기준으로 JOIN하는지에 따라 분석 대상 고객이 달라질 수 있으므로 key 관계와 데이터 포함 범위를 먼저 확인해야 한다.


## 8. 자소서·면접 활용 포인트

- 문서나 컬럼명만 믿지 않고 실제 데이터의 유일성, 중복, key 포함관계를 검증한 경험
- demographic이 전체 거래 고객을 포함하지 않는다는 점을 확인해 분석 모집단 문제를 인식한 경험
- 예상 grain과 실제 데이터 구조가 다른 문제를 실제 중복 행 확인으로 해결한 경험
- KaggleHub, `.venv`, `requirements.txt`, Git을 이용해 재현 가능한 분석 환경을 구축한 경험