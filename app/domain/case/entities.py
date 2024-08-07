from dataclasses import dataclass, field


@dataclass
class TemplateCreationResponse:
    location: str
    message: str = field(init=False)

    def __post_init__(self):
        self.message = f"Event from {self.location} location was created"