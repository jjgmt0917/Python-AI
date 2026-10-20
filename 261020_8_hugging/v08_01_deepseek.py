import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
)

q = input("질문을 입력해주세요: ")
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1:novita",
    messages=[
        {
            "role": "user",
            "content": q
        }
    ],
)

print(completion.choices[0].message)

# [출력결과]
# 질문을 입력해주세요: hi
# ChatCompletionOutputMessage(role='assistant', content="\nHi there! 👋 How can I help you today? Whether you have a question, need advice, or just want to chat—I'm all ears! 😊  \nTell me what's on your mind! 🌟", reasoning=None, tool_call_id=None, tool_calls=None, reasoning_content='\n嗯，用户发来一个简单的“hi”。看起来是个很常见的开场白，可能刚打开聊天界面想测试功能，或者一时没想好具体要问什么。\n\n用户情绪应该比较放松，用这种随意的打招呼方式可能想建立轻松的氛围。说不定是第一次使用这类AI助手，带着好奇心想试试看。也可能是老用户懒得打字，随手发个hi等我来引导对话。\n\n这种情况下不适合直接问“有什么需要帮助吗”这么正式。用同样活泼的“Hi”回应能降低距离感，加上表情符号传递友好态度。后半句特意用“告诉我吧”的主动句式，比“请问需要什么”更亲切，给用户自由发挥的空间。\n\n对了，结尾用星星符号代替句号，让整个回复显得更温暖。用户如果真有需求自然会接话，如果只是打招呼也不会冷场。\n')
