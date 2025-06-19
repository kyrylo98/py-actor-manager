from dataclasses import dataclass


@dataclass
class Actor:
    def __init__(self, id: int, first_name: str, last_name: str) -> None:
        self.id = id
        self.firstName = first_name
        self.last_name = last_name
