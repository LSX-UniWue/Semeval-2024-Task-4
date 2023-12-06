from pathlib import Path


def get_project_root() -> Path:
    """
    :return: The path to the root directory of this project
    """
    return Path(__file__).parent.parent
