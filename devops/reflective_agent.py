from .agent import DevOpsAspect, Solution
from ..core.base_agent import BaseAgent

class DevOpsReflectiveAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.aspects_checklist = {aspect: False for aspect in DevOpsAspect}

    def analyze_question(self, question: str) -> Dict:
        """
        Break down the question and identify relevant DevOps aspects
        """
        analysis = {
            'primary_aspects': [],
            'related_aspects': [],
            'constraints': [],
            'requirements': [],
            'context': {}
        }
        
        self._reflect_on_question(question, analysis)
        return analysis

    def _reflect_on_question(self, question: str, analysis: Dict) -> None:
        reflection_questions = [
            "What is the core problem being addressed?",
            "What are the implicit requirements?",
            "What constraints might not be explicitly stated?",
            "What DevOps best practices apply here?",
            "What could go wrong with potential solutions?",
            "Are there any compliance or security implications?",
            "What dependencies need to be considered?",
            "How will this scale in the future?"
        ]
        
        for reflection in reflection_questions:
            self._consider_aspect(reflection, analysis) 