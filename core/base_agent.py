from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def analyze_question(self, question: str):
        pass

    @abstractmethod
    def _reflect_on_question(self, question: str, analysis: Dict):
        pass 