from transformers import AutoTokenizer


class AutoChatTokenizer():
    def __init__(self, 
                 pretrained_model_name_or_path, 
                 template=None,
                 *args,
                 **kwargs):
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path, *args, **kwargs)
        self.has_chat_template = self.tokenizer.chat_template != None

        if not self.has_chat_template:
            raise Exception("The tokenizer does not have a chat_template. Auto apply of the chat template is not possible.")
    
    def prompt(self,
               text,
               tokenize=False,
               add_generation_prompt=True,
               *args,
               **kwargs):
        messages = [
            {'role': 'user', 'content': text}
        ]
        return self.chat(messages, tokenize=tokenize, add_generation_prompt=add_generation_prompt, *args, **kwargs)

    def chat(self,
             messages,
             tokenize=False,
             add_generation_prompt=True,
             *args,
             **kwargs):
        return self.tokenizer.apply_chat_template(messages, tokenize=tokenize, add_generation_prompt=add_generation_prompt, *args, **kwargs)