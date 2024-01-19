import os
import fnmatch
import yaml
from typing import List, Dict

def load_configuration(config_file: str = 'config.yaml') -> Dict:
    """Load configuration from a YAML file.

    Args:
        config_file (str): Path to the configuration file.

    Returns:
        Dict: Configuration data.
    """
    with open(config_file, 'r') as file:
        return yaml.safe_load(file).get('repo_loader_config', {})

def get_ignore_patterns(ignore_file_path: str) -> List[str]:
    """Read ignore patterns from a file.

    Args:
        ignore_file_path (str): Path to the ignore file.

    Returns:
        List[str]: List of ignore patterns.
    """
    if not os.path.exists(ignore_file_path):
        return []

    with open(ignore_file_path, 'r') as file:
        return [line.strip().replace("/", "\\") if os.name == "nt" else line.strip()
                for line in file]

def is_ignored(file_path: str, ignore_patterns: List[str]) -> bool:
    """Check if a file path matches any of the ignore patterns.

    Args:
        file_path (str): The file path to check.
        ignore_patterns (List[str]): List of ignore patterns.

    Returns:
        bool: True if file should be ignored, False otherwise.
    """
    return any(fnmatch.fnmatch(file_path, pattern) for pattern in ignore_patterns)

def process_repository(repo_path: str, ignore_patterns: List[str], output_file_path: str) -> None:
    """Process files in a repository and write content to an output file.

    Args:
        repo_path (str): Path to the repository.
        ignore_patterns (List[str]): Patterns to ignore.
        output_file_path (str): Path to the output file.
    """
    with open(output_file_path, 'w') as output_file:
        for root, _, files in os.walk(repo_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_file_path = os.path.relpath(file_path, repo_path)

                if not is_ignored(relative_file_path, ignore_patterns):
                    with open(file_path, 'r', errors='ignore') as file:
                        contents = file.read()
                    output_file.write("-" * 4 + "\n")
                    output_file.write(f"{relative_file_path}\n")
                    output_file.write(f"{contents}\n")
        output_file.write("--END--")

if __name__ == "__main__":
    config = load_configuration()
    repo_path = config['repo_path']
    output_file_name = config['output_file_name']
    ignore_file_path = config.get('ignore_file_path', '.gptignore')

    ignore_patterns = get_ignore_patterns(ignore_file_path)
    process_repository(repo_path, ignore_patterns, output_file_name)

    print(f"Repository contents written to {output_file_name}.")
