# 🦦✨ OtterlyObsessedWithSemantics ✨🦦

This repo contains our submission for Semeval 2024 Task 4.<br>
Feel free to take a deep dive 🦦🌊

## Setup 🦦
### Install Requirements 🚀
Using pip and Python3.10.0
```
pip install -r requirements.txt
```

### Data 📊
1. Get data from the [Task Site](https://propaganda.math.unipd.it/semeval2024task4/)
1. Load data into data directory:
    ```
    data
    └── subtask1
        ├── dev.json
        ├── dev_unlabeled.json
        ├── train.json
        └── validation.json
    ```
1. Run preprocessing
   ```
    python3 -m src.classes.preprocess
   ```

## Training 🏋️
Execute the notebook: [src/tune_classification_model.ipynb](src/tune_classification_model.ipynb)<br>
✨Parameters✨ can be changed in the run-config:
- `dataset_style`: Either `cleaned` or `all_lower`
- `model_name`: Huggingface identifier for the model (like `bert-base-cased`)
- `use_custom_head`: Whether to use the custom head we developed (`True`or `False`)
- `use_hierarchy`: Whether to use the hierarchy instead of only the leaves (`True` or `False`)
- `extra_lazers`: Whether to add additional linear layers in the custom head (`True` or `False`)
- `weight_loss`: Whether to weight the classes based on their inverse frequencies in the cross entropy loss calculation (`True`or `False`)
- `epochs`: Number of training epochs
- `lr`: Learning rate
- `batch_size`: For the GPU
- `acc_steps`: Accumulation steps
- `seed`: Set random seed
- `limit`: Only train on a subset of the data (`int` or `None` to use the full dataset)
