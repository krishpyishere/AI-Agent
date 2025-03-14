from typing import Dict, List, Optional
from enum import Enum
from dataclasses import dataclass
import logging

class DevOpsAspect(Enum):
    INFRASTRUCTURE = "infrastructure"
    SECURITY = "security"
    AUTOMATION = "automation"
    MONITORING = "monitoring"
    PERFORMANCE = "performance"
    SCALABILITY = "scalability"
    RELIABILITY = "reliability"
    COST_OPTIMIZATION = "cost_optimization"
    COMPLIANCE = "compliance"
    CI_CD = "ci_cd"

@dataclass
class Solution:
    description: str
    implementation_steps: List[str]
    considerations: List[str]
    risks: List[str]
    estimated_effort: str
    tools_required: List[str]
    prerequisites: List[str]
    validation_steps: List[str] 