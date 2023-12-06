import json
import os.path

from src.classes.alphabet import Alphabet
from src.classes.data_tuple import DataTuple
from src.path_utils import get_project_root


class SemevalDataset:
    def __init__(self, split: str, style: str):
        with open(os.path.join(get_project_root(), f'data/preprocessed_data/{style}/{split}.json'), 'r') as f:
            data = json.load(f)
            print(f'First sample: {data[0]}')
            self.samples = [DataTuple(item['text'], item['labels'], item['id']) for item in data]

        # Create alphabet and add all labels to the alphabet
        self.alphabet = Alphabet()
        [[self.alphabet.add_label(lbl) for lbl in sample.labels] for sample in self.samples]
