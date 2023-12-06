from dataclasses import dataclass


@dataclass
class DataTuple:
    text: str
    labels: list[str]
    meme_id: int
