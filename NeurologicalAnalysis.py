class Ailment:
    def __init__(self, name: str, symptoms=None, cures=None, precautions=None):
        """
        Represents a neurological ailment with associated symptoms, cures
        and precautions.

        :param name: Name of the ailment
        :param symptoms: List of symptoms (strings)
        :param cures: List of cures (strings)
        :param precautions: List of precautions (strings)
        """

        self.name = name
        self.symptoms = symptoms or []
        self.cures = cures or []
        self.precautions = precautions or []

    def add_symptom(self, symptom: str):
        if symptom not in self.symptoms:
            self.symptoms.append(symptom)

    def add_cure(self, cure: str):
        if cure not in self.cures:
            self.cures.append(cure)
    
    def add_precaution(self, precaution: str):
        if precaution not in self.precautions:
            self.precautions.append(precaution)

    def summary(self) -> str:
        """Return a formatted summary of the ailment and its info."""
        lines = [
            f"Ailment: {self.name}",
            "Symptoms:",
            *(f" - {s}" for s in self.symptoms),
            "Cures:",
            *(f" - {c}" for c in self.cures),
            "Precautions:",
            *(f" - {p}" for p in self.precautions)
        ]
        return "\n".join(lines)
    
    def to_dict(self) -> dict:
        """Convert the ailment data to a dictionary"""
        return {
            "name": self.name,
            "symptoms": list(self.symptoms),
            "cures": list(self.cures),
            "precautions": list(self.precautions),
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create an Ailment from a dict"""
        return cls(
            name=d.get("name", ""),
            symptoms=d.get("symptoms", []),
            cures=d.get("cures", []),
            precautions=d.get("precautions", []),
        )