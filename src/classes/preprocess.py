import json
import os
import re
import shutil

from src.path_utils import get_project_root


def clean_text(text):
    text = re.sub(r"(\\\\n)+", ' ', text)
    text = re.sub(r"(\\n)+", ' ', text)
    text = re.sub(r"\s+", ' ', text)
    return text


def preprocess_data():
    # Original, cleaned, all_lower, no_stopwords, everything
    for idx in range(5):
        suffix = 'original' if idx == 0 else ''
        suffix = 'cleaned' if idx == 1 else suffix
        suffix = 'all_lower' if idx == 2 else suffix
        suffix = 'no_stopwords' if idx == 3 else suffix
        suffix = 'all_lower_no_stopwords' if idx == 4 else suffix

        # Setup out dir
        preprocessed_path = os.path.join(get_project_root(), 'data', 'preprocessed_data', suffix)
        if os.path.isdir(preprocessed_path):
            shutil.rmtree(preprocessed_path)
        os.makedirs(preprocessed_path)

        # Create semeval_dataset
        for split in ['train', 'validation', 'dev']:

            # Load raw data
            with open(os.path.join(get_project_root(), 'data', 'subtask1', f'{split}.json'), 'r') as f:
                raw_data = json.load(f)

            preprocessed_data = []
            for sample in raw_data:
                processed_text = sample['text']

                if 'original' not in suffix:
                    processed_text = clean_text(processed_text)
                if 'all_lower' in suffix:
                    processed_text = processed_text.lower()

                sample['text'] = processed_text
                preprocessed_data.append(sample)

            with open(os.path.join(preprocessed_path, f'{split}.json'), 'w') as f:
                json.dump(preprocessed_data, f)

            print(f'-' * 20 + f'\nStyle: {suffix}\n' + '-' * 20)
            for sample in preprocessed_data[:5]:
                print(sample["text"])


if __name__ == '__main__':
    preprocess_data()
