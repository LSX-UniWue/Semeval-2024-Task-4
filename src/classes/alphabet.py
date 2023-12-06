class Alphabet:
    """Stores a mapping between labels and indices"""

    id2lbl = {}
    lbl2id = {}

    def labels(self) -> list[str]:
        return list(self.lbl2id.keys())

    def add_label(self, label: str):
        if label in self.lbl2id.keys():
            # Label is known
            return

        new_id = len(self.id2lbl)
        self.id2lbl[new_id] = label
        self.lbl2id[label] = new_id
