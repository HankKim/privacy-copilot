import ollama

def analyze_with_ai(text):
    prompt = f"""
당신은 개인정보보호 컨설턴트입니다.

다음 개인정보처리방침을 검토하세요.

다음 형식으로 답변하세요.

1. 잘 작성된 점
2. 부족한 점
3. 개선 권고사항(3개 이내)

문서:
{text}
"""

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]