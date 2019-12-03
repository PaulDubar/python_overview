class Question: # a multi-choice question object will have question prompt and an answer
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
