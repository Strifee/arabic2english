from train import BATCH_SIZE


class Hyperparam:
    """Hyper parameters"""
    # Training
    BATCH_SIZE = 32
    learning_rate = 0.0002
    num_epochs = 50

    # Model
    num_heads = 8
    num_encoder_layers = 3
    num_decoder_layers = 3

    max_len= 50
    dropout = 0.4
    embedding_size= 256
