import json
import os
from common.ai_engine import GeminiEngine
from infra.db_manager import DBManager
from models.schemas import FinancialDocSchema
from config.settings import config

from config.settings import config


def run_doc_validator():
    db = DBManager()
    db.init_tables()
    engine = GeminiEngine()

    sample_dir = config.BASE_DIR / "data" / "samples"

    if not sample_dir.exists():
        sample_dir.mkdir(parents=True, exist_ok=True)
        print(f"폴더가 없어서 생성했습니다: {sample_dir}")
        return

    extensions = (".png", ".jpg", ".jpeg")
    image_files = [f for f in os.listdir(sample_dir) if f.lower().endswith(extensions)]

    if not image_files:
        print(f"{sample_dir}' 폴더에 처리할 이미지 파일이 없습니다")
        return
    print(f"총 {len(image_files)}개의 파일을 발견했습니다. 분석을 시작합니다.")

    for file_name in image_files:
        print(f"\n--- [작업 시작: {file_name}] ---")
        image_path = sample_dir / file_name

        prompt = "이 금융 문서의 정보를 추출해서 JSON으로 줘. (doc_type, amount, currency, doc_date, account_number)"

        try:
            raw_result = engine.analyze_document(str(image_path), prompt)

            if not raw_result:
                print(f"AI 응답이 비어있습니다.")
                continue
            print(f"AI 응답 수신 완료!")
            print(f"🔍 AI가 보낸 답변 내용:\n{raw_result}")
            import re

            json_match = re.search(r"\{.*\}", raw_result, re.DOTALL)

            if json_match:
                clean_json = json_match.group()
                data_dict = json.loads(clean_json)

                validated_data = FinancialDocSchema(**data_dict)

                # DB 저장
                db.insert_doc(validated_data)
                print(f"{file_name} 처리 완료 및 DB 저장 성공")

        except Exception as e:
            print(f"{file_name} 처리 중 에러: {e}")


if __name__ == "__main__":
    run_doc_validator()
