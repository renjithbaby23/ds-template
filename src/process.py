"""This is the demo code that uses hydra.

Hydra helps to access the parameters in under the directory config.
"""

import hydra
from hydra.utils import to_absolute_path as abspath
from omegaconf import DictConfig


@hydra.main(config_path="../config", config_name="main")
def process_data(config: DictConfig):
    """Process the training data."""
    raw_path = abspath(config.raw.path)
    print(f"Process data using {raw_path}")
    print(f"Columns used: {config.process.use_columns}")


if __name__ == "__main__":
    process_data()
