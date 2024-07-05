# auto-chat-template
Automatically Applying Chat Templates for LLMs

## Installation

`pip install git+https://github.com/taeminlee/auto-chat-template`

## Usage

```python
from auto_chat_template import AutoChatTokenizer

act = AutoChatTokenizer('taeminlee/KULLM3-awq')
ctx = act.prompt('hello world')
# <s>[INST] <<SYS>>\n당신은 고려대학교 NLP&AI 연구실에서 만든 AI 챗봇입니다. 당신의 이름은 'KULLM'으로, 한국어로는 '구름'을 뜻합니다. 당신은 비도덕적이거나, 성적이거나, 불법적이거나 또는 사회 통념적으로 허용되지 않는 발언은 하지 않습니다. 사용자와 즐겁게 대화하며, 사용자의 응답에 가능한 정확하고 친절하게 응답함으로써 최대한 도와주려고 노력합니다. 질문이 이상하다면, 어떤 부분이 이상한지 설명합니다. 거짓 정보를 발언하지 않도록 주의합니다.\n<</SYS>>\n\nhello world [/INST]
```
