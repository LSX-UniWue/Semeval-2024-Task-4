from dataclasses import dataclass


@dataclass
class RunConfig:
    dataset_style: str = 'cleaned'
    model_name: str = 'bert-base-cased'
    use_custom_head: bool = True
    freeze_base_model: bool = False
    weight_loss: bool = False
    extra_layers: bool = False
    use_hierarchy: bool = True
    epochs: int = 3
    lr: float = 5e-5
    batch_size: int = 8
    acc_steps: int = 3
    seed: int = 42

    limit: int | None = 200

    def identifier(self) -> str:
        identifier_str = (f"Style_{self.dataset_style}_Model_{self.model_name}_CustomHead_{self.use_custom_head}_"
                          f"ExtraLayers_{self.extra_layers}_"
                          f"FreezeBase_{self.freeze_base_model}_"
                          f"Weight_Loss_{self.weight_loss}_"
                          f"Hierarchy_{self.use_hierarchy}_Epochs_{self.epochs}_"
                          f"LR_{self.lr}_Limit_{self.limit}_Seed_{self.seed}")

        # Replacing characters that are not safe for file names
        for char in ['\\', '/', ':', '*', '?', '"', '<', '>', '|']:
            identifier_str = identifier_str.replace(char, '_')

        return identifier_str
