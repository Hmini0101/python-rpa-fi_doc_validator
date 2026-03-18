# 📄 Python RPA - Financial Document Validator

> **Gemini 2.0 기반 금융 문서 자동 분석 및 데이터베이스 저장 도구**

이 프로젝트는 영수증, 청구서 등의 금융 문서 이미지를 AI(Gemini 2.0 Flash)로 분석하여 필요한 데이터를 추출하고, 이를 구조화하여 SQLite 데이터베이스에 자동으로 저장하는 RPA(Robotic Process Automation) 시스템입니다.

---

## ✨ 주요 기능

* **AI 기반 문서 분석**: `gemini-2.0-flash` 모델을 사용하여 영수증 이미지 내 텍스트 인식 및 항목별 데이터 정형화.
* **자동 배치 처리**: `data/samples` 폴더에 이미지를 넣기만 하면 모든 파일을 순회하며 자동 처리.
* **데이터 검증**: `Pydantic` 스키마를 활용해 금액, 날짜 등 데이터 타입의 무결성 보장.
* **DB 영구 저장**: 분석된 데이터를 `SQLite 3` 데이터베이스에 체계적으로 기록.

---

## 🛠 기술 스택

| 분류 | 기술 |
| :--- | :--- |
| **Language** | Python 3.11+ |
| **AI Engine** | Google Generative AI (Gemini 2.0 Flash) |
| **Data Validation** | Pydantic v2 |
| **Database** | SQLite 3 |
| **Environment** | venv (Virtual Environment) |

---

## 📂 프로젝트 구조

```text
python-rpa-fi_doc_validator/
├── common/             # AI 엔진(Gemini) 인터페이스
├── config/             # 환경 변수 및 공통 설정
├── data/               
│   ├── samples/        # 분석할 이미지(영수증 등) 보관 폴더
│   └── finance_data.db # 최종 분석 데이터가 저장되는 DB
├── infra/              # 데이터베이스 매니저 (CRUD 로직)
├── models/             # Pydantic 데이터 모델 (Schemas)
├── jobs/               
│   └── doc_validator/  # 메인 실행 비즈니스 로직
└── .env                # API Key 보안 설정 파일
```
---

👤 작성자<br>
현민 (HyeonMin)<br>
RPA Developer / Process Automation Engineer
