
# dunnhumby CRM Analytics Project Master

## 1. 프로젝트 목적

dunnhumby `The Complete Journey` 데이터를 활용해 CRM / Customer Analytics 분석 과정을 직접 수행한다.

단순히 결과물을 만드는 것이 아니라 DB, ERD, SQL, 고객 분석, CRM 지표를 실제 데이터로 학습하고, 모르는 개념은 직접 검증하며 진행한다.

최종적으로 다음 역량을 갖추는 것을 목표로 한다.

- 고객 데이터 구조 이해
- 관계형 데이터베이스와 ERD 이해
- SQL 기반 고객 데이터 추출
- 고객 행동 분석 및 CRM 가설 수립
- 분석 결과를 CRM 의사결정과 연결
- 재현 가능한 분석 프로젝트 관리
- 프로젝트 경험을 자소서·면접에 활용


## 2. 프로젝트 진행 원칙

### 학습 우선
모르는 개념은 넘어가지 않고 개념 이해 → 예제 확인 → 실제 데이터 검증 → 분석 적용 순서로 학습한다.

### 검증 우선
컬럼명이나 문서 설명만으로 데이터 구조를 단정하지 않고 실제 데이터의 유일성, 중복, 포함관계를 확인한다.

### 재현 가능성
원본 데이터는 GitHub에 업로드하지 않고 KaggleHub로 다운로드한다. 코드, SQL, 문서, 환경 설정을 Git으로 관리한다.

### 기록
분석 결과뿐 아니라 주요 의사결정, 문제 해결 과정, AI 활용, 직무 관점에서의 학습을 기록한다.


## 3. 데이터

Dataset: dunnhumby - The Complete Journey

Kaggle:
`frtgnn/dunnhumby-the-complete-journey`

데이터 경로:

- 원본: `data/raw/`
- 가공: `data/processed/`

원본 및 가공 데이터는 Git에서 추적하지 않는다.


## 4. 프로젝트 구조

```text
dunnhumby-crm-analytics/
├── PROJECT_MASTER.md
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── day_logs/
│   └── erd/
├── notebooks/
├── sql/
└── src/
```


## 5. 진행 현황

| Day | 주제 | 상태 |
|---|---|---|
| Day 0 | Git / GitHub 및 프로젝트 환경 구축 | 완료 |
| Day 1 | 데이터 구조 이해 및 ERD 작성 | 진행 중 |
| Day 2 이후 | Day 1 완료 후 구체화 | 예정 |


## 6. 주요 의사결정

### Decision 001 — 데이터 관리
원본 및 가공 데이터는 GitHub에 올리지 않고 KaggleHub를 통해 재현 가능하게 관리한다.

### Decision 002 — 학습 중심 진행
결과물을 빠르게 만드는 것보다 CRM / Customer Analytics 분석 과정을 제대로 이해하는 것을 우선한다.

### Decision 003 — 데이터 구조 검증
ERD와 JOIN 관계는 컬럼명만 보고 정의하지 않고 실제 유일성, 중복, key 포함관계를 검증한 뒤 결정한다.

### Decision 004 — 분석 환경
Python 패키지는 프로젝트 전용 `.venv`에서 관리하고 `requirements.txt`에 필요한 패키지를 기록한다.


## 7. Day별 요약

### Day 0 — 프로젝트 환경 구축

- Git / GitHub 기본 흐름 학습
- 로컬 repository와 GitHub 연결
- `.gitignore` 설정
- 프로젝트 기본 폴더 구조 생성
- 원본 데이터를 Git에서 제외하도록 설정


### Day 1 — 데이터 구조 이해 및 키 관계 검증

#### 완료
- Python 3.14 기반 `.venv` 구성
- KaggleHub로 dunnhumby 데이터 다운로드
- 8개 테이블의 컬럼 및 grain 확인
- PK / FK / 복합키 후보 검증
- household 및 product key 포함관계 확인
- `coupon` 중복 데이터와 `causal_data` grain 이슈 확인

#### 핵심 학습
- PK, FK, 복합키, grain, 참조 무결성 개념 이해
- key 개수 비교보다 실제 집합 포함관계를 확인해야 함
- 개념적으로 예상한 grain과 실제 데이터의 물리적 grain이 다를 수 있음
- JOIN 전에 분석 모집단과 key 관계를 확인해야 함

#### 주요 의사결정
- `hh_demographic`을 전체 고객 마스터로 보지 않음
- ERD는 실제 데이터 검증 결과를 기준으로 작성

#### 문제 해결
- KaggleHub 다운로드 오류 → `data/raw`의 테스트 파일 제거
- `causal_data` 예상 grain 불일치 → 실제 중복 행 확인 후 grain 재정의

#### 직무·자소서 포인트
- 고객 분석 전에 데이터 구조와 모집단 정의가 중요하다는 점을 체감
- 문서나 컬럼명만 믿지 않고 실제 key 관계를 검증한 경험

상세 기록: `docs/day_logs/day01.md`
