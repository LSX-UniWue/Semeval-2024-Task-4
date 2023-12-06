import torch


class TheOtterBertModel(torch.nn.Module):
    """Defines a custom classification head for a BertModel with dropout layers."""

    def __init__(self, embedding_size, output_sizes, dropout_prob=0.2, extra_layers: bool = False):
        super(TheOtterBertModel, self).__init__()

        self.layers = torch.nn.ModuleList()
        self.dropouts = torch.nn.ModuleList()
        self.activations = torch.nn.ModuleList()

        self.extra_layers = extra_layers

        if extra_layers:
            self.embedding_additions = torch.nn.ModuleList()
            self.embedding_additions.append(torch.nn.Linear(embedding_size, embedding_size))
            self.embedding_additions.append(torch.nn.Dropout(dropout_prob))
            self.embedding_additions.append(torch.nn.LeakyReLU())
            self.embedding_additions.append(torch.nn.Linear(embedding_size, embedding_size))
            self.embedding_additions.append(torch.nn.Dropout(dropout_prob))
            self.embedding_additions.append(torch.nn.LeakyReLU())

        for output_size in output_sizes:
            self.layers.append(torch.nn.Linear(embedding_size, output_size))
            self.dropouts.append(torch.nn.Dropout(dropout_prob))
            self.activations.append(torch.nn.LeakyReLU())
            embedding_size += output_size

    def forward(self, cls_embedding):

        if len(cls_embedding.shape) == 3:
            # We need to extract the first dim as this is the cls token
            cls_embedding = cls_embedding[:, 0, :]

        all_decisions = []
        x = cls_embedding

        if self.extra_layers:
            for layer in self.embedding_additions:
                x = layer(x)

        for layer, dropout, activation in zip(self.layers, self.dropouts, self.activations):
            x = layer(x)
            # x = dropout(x)
            # x = activation(x)
            all_decisions.append(x)

            # Concatenate the decision with the original CLS embedding for the next layer
            x = torch.cat((cls_embedding, *all_decisions), dim=1)

        final_decision = torch.cat(all_decisions, dim=1)

        return final_decision
