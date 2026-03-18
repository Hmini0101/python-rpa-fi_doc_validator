import google.generativeai as genai
from config.settings import config
import PIL.Image


class GeminiEngine:
    def __init__(self):
        genai.configure(api_key=config.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel("gemini-flash-latest")

    def analyze_document(self, image_path: str, prompt: str):
        try:
            img = PIL.Image.open(image_path)
            response = self.model.generate_content([prompt, img])
            return response.text
        except Exception as e:
            return f"AI 분석 중 에러 발생: {e}"
