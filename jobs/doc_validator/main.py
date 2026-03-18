from common.ai_engine import GeminiEngine
import os


def run():
    engine = GeminiEngine()

    image_path = "data/samples/test_receipt.jpg"

    if not os.path.exists(image_path):
        print(f"파일을 찾을 수 없습니다: {image_path}")
        return

    prompt = """
    이 금융 문서를 분석해서 다음 정보를 추출해줘. 
    반드시 JSON 형식으로만 대답해:
    {
        "doc_type": "문서종류",
        "amount": 10000,
        "currency": "KRW",
        "doc_date": "YYYY-MM-DD",
        "is_valid": true
    }
    """

    print("AI가 서류를 분석중입니다.")
    result = engine.analyze_document(image_path, prompt)
    print("\n--- [분석 결과] ---")
    print(result)


if __name__ == "__main__":
    run()
