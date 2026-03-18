import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. .env 파일 로드
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ 에러: .env 파일에서 GOOGLE_API_KEY를 찾을 수 없습니다!")
else:
    print(f"✅ 키 로드 성공: {api_key[:10]}****************")

    # 2. API 설정
    genai.configure(api_key=api_key)

    try:
        # 3. 사용 가능한 모델 리스트 출력
        print("\n--- [접근 가능한 모델 목록] ---")
        available_models = []
        for m in genai.list_models():
            if "generateContent" in m.supported_generation_methods:
                print(f"👉 {m.name}")
                available_models.append(m.name)

        if not available_models:
            print(
                "⚠️ 경고: 사용할 수 있는 모델이 하나도 없습니다. API 키 권한을 확인하세요."
            )
        else:
            # 4. 간단한 테스트 (Hello World)
            print("\n--- [연결 테스트 시작] ---")
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content("안녕? 너는 누구니?")
            print(f"🤖 AI 응답: {response.text}")
            print("\n✨ 모든 설정이 완벽합니다!")

    except Exception as e:
        print(f"\n❌ API 호출 중 에러 발생: {e}")
