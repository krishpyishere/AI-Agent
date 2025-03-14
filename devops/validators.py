from typing import List
from .agent import Solution

class DevOpsValidator:
    @staticmethod
    def validate_security(solution: Solution) -> List[str]:
        security_checks = [
            "Authentication mechanisms",
            "Authorization controls",
            "Data encryption",
            "Network security",
            "Secret management",
            "Compliance requirements",
            "Security scanning",
            "Vulnerability management"
        ]
        
        findings = []
        for check in security_checks:
            if not any(check.lower() in step.lower() for step in solution.implementation_steps):
                findings.append(f"Missing {check} consideration")
        
        return findings

    @staticmethod
    def validate_reliability(solution: Solution) -> List[str]:
        reliability_checks = [
            "High availability",
            "Disaster recovery",
            "Backup strategies",
            "Failover mechanisms",
            "Load balancing",
            "Circuit breakers",
            "Rate limiting"
        ]
        
        findings = []
        for check in reliability_checks:
            if not any(check.lower() in step.lower() for step in solution.implementation_steps):
                findings.append(f"Consider adding {check}")
        
        return findings 