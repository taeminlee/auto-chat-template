import re


class TemplateBase():
    template = """jinja2 template here"""
    model_name_patterns = [r"pattern here"]

    @classmethod
    def match(cls, pretrained_model_name_or_path):
        return any(re.search(pattern, pretrained_model_name_or_path) for pattern in cls.model_name_patterns)