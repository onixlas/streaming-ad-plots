import json
import os
from pathlib import Path

from matplotlib.figure import Figure


def load_config(config_path: str | Path="config.json") -> dict:
    """Load visualization configuration from JSON file.
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Dictionary with all visualization settings
        
    Raises:
        FileNotFoundError: If config file doesn't exist
        json.JSONDecodeError: If config file is malformed
    """
    with open(config_path, "r") as f:
        config = json.load(f)
    return config

def save_plot(fig: Figure, name: str, config: dict):
    """Save matplotlib figure according to configuration.
    
    Args:
        fig: Matplotlib figure to save
        name: Base name for the file (without extension)
        config: Loaded configuration dictionary
        
    Returns:
        Path to the saved file
        
    Raises:
        OSError: If output directory cannot be created
    """
    output_cfg = config["visualization"]["output"]
    os.makedirs(output_cfg["folder"], exist_ok=True)
    filename = f"{name}.{output_cfg['format']}"
    path = Path(output_cfg["folder"]) / filename
    fig.savefig(
        path,
        dpi=output_cfg["dpi"],
        bbox_inches="tight",
        format=output_cfg["format"]
    )
    return path
