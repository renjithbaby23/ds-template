"""This is the demo code that uses Hydra.

Hydra is used to access the parameters in under the directory config.
"""

import hydra
from hydra.utils import to_absolute_path as abspath
from omegaconf import DictConfig


@hydra.main(version_base=None, config_path="../config", config_name="main")
def train_model(config: DictConfig):
    """Trains the model."""
    input_path = abspath(config.processed.path)
    output_path = abspath(config.final.path)

    print(f"Train modeling using {input_path}")
    print(f"Model used: {config.model}")

    print(f"Save the output to {output_path}")


if __name__ == "__main__":
    train_model()
