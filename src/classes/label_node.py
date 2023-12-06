from dataclasses import dataclass


@dataclass
class LabelNode:
    text: str
    parents: list['LabelNode']
