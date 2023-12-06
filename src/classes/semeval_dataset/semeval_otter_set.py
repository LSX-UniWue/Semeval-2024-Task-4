import json
import os

from src.classes.alphabet import Alphabet
from src.classes.data_tuple import DataTuple
from src.classes.label_hierarchy import LabelHierarchy
from src.path_utils import get_project_root


class SemevalOtterSet:

    def __init__(self, split: str, style: str):
        split_path = os.path.join(get_project_root(), 'data', 'preprocessed_data', style, f'{split}.json')
        assert os.path.isfile(split_path), f'Did not find dataset at path: {split_path}'

        # Create label hierarchy
        self.lh = LabelHierarchy()

        # Load the file
        with open(split_path, 'r') as f:
            data = json.load(f)

            self.samples: list[DataTuple] = []
            print(f'First entry: {data[0]}')

            for entry in data:
                parents = list(
                    set(sum([self.lh.get_parent_labels_flat(self.lh.get_node_by_label(lbl)) for lbl in entry['labels']],
                            [])))
                self.samples.append(DataTuple(entry['text'], parents, entry['id']))

        # Create alphabet and add all labels to the alphabet
        self.alphabet = Alphabet()

        labels_ordered = ['Ethos', 'Pathos', 'Logos', 'Ad Hominem', 'Justification', 'Reasoning', 'Distraction',
                          'Simplification']
        other_labels = list(set(sum([sample.labels for sample in self.samples], [])))
        labels_ordered += [lbl for lbl in other_labels if lbl not in labels_ordered]
        [self.alphabet.add_label(lbl) for lbl in labels_ordered]


if __name__ == '__main__':
    otter_set = SemevalOtterSet('train')
    print(f'Alphabet Labels: {otter_set.alphabet.labels()}')
