import fire
from auto_chat_template.auto_chat_tokenizer import AutoChatTokenizer


class AutoChatTemplate:
    def __init__(self):
        pass

    def prompt(self, 
               pretrained_model_name_or_path='nlpai-lab/KULLM3', 
               text='Hello World',
               tokenize=False,
               add_generation_prompt=True,
               template=None,
               *args,
               **kwargs):
        chat_tokenizer = AutoChatTokenizer(pretrained_model_name_or_path=pretrained_model_name_or_path, template=template)
        print(chat_tokenizer.prompt(text, tokenize=tokenize, add_generation_prompt=add_generation_prompt, *args, **kwargs))

    def chat(self, 
               pretrained_model_name_or_path='nlpai-lab/KULLM3', 
               messages=[{'role': 'user', 'content': 'Hello World!'},{'role': 'assistant', 'content': 'Hi!'},{'role': 'user', 'content': 'Wow!'}],
               tokenize=False,
               add_generation_prompt=True,
               template=None,
               *args,
               **kwargs):
        chat_tokenizer = AutoChatTokenizer(pretrained_model_name_or_path=pretrained_model_name_or_path, template=template)
        print(chat_tokenizer.chat(messages, tokenize=tokenize, add_generation_prompt=add_generation_prompt, *args, **kwargs))


def main():
    fire.Fire(AutoChatTemplate)

if __name__ == '__main__':
    main()