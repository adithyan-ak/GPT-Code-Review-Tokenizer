# GPT Code Review Tokenizer

This tool is designed for efficiently processing and tokenizing large code repositories. It consists of two main components: `load_repository.py` and `tokenizer.py`. The first component scans a specified repository, filters files based on ignore patterns, and outputs its contents into a single file. The second component then tokenizes this output into smaller, manageable chunks suitable to perform code reviews with GPTs.

## Features

*   **Repository Scanning**: Traverses every file in a specified repository path.
*   **Ignore Pattern Filtering**: Optionally ignores files matching specified patterns.
*   **Output Consolidation**: Aggregates repository contents into a single file.
*   **Tokenization**: Splits the repository's contents into tokenized chunks.
*   **Customizable Tokenization**: Allows setting of maximum tokens per chunk.

## Installation

1.  Clone the repository: `git clone [repository-url]`
2.  Navigate to the project directory: `cd [project-directory]`
3.  Ensure Python 3.x is installed.
4.  Install required packages: `pip3 install -r requirements.txt`

## Usage

1.  Configure the `config.yaml` file according to your requirements.
    *   Set the `repo_path` to the target repository.
    *   Optionally set `ignore_file_path` to specify patterns to ignore. By default, `.gptignore` contains commonly ignored files.
    *   Configure `tokenizer_config` for tokenization settings.
2.  Run `python3 load_repository.py` to process the repository and generate the `output.txt` file.
3.  Run `python3 tokenizer.py` to tokenize the processed output.

## Contributions
We welcome contributions! If you have a feature to add or found a bug, please submit a pull request or open an issue.

The following are some of the features we are working on and would love help with:

- [ ] **Configurable Output Formats**: Allow users to choose different output formats (e.g., JSON, XML) for the tokenized data, catering to various use cases.
- [ ] **Error Handling and Logging**: Improve error handling and add comprehensive logging to help users troubleshoot issues during repository processing and tokenization.
- [ ] **Testing and Quality Assurance**: Develop a suite of tests (unit, integration, performance) to ensure code quality and facilitate safe refactoring.
- [ ] **Documentation Enhancements**: Improve and expand the documentation, including detailed setup guides, use case examples, and FAQs.
- [ ] **Dockerization**: Containerize the application using Docker for easy deployment and execution across different environments.

## Authors

* [Adithyan AK](https://www.linkedin.com/in/akinfosec/)
* [Gowthamaraj Rajendran](https://www.linkedin.com/in/gowthamaraj-rajendran/)

## Acknowledgements

*  [mpoon - gpt3-repository-loader](https://github.com/mpoon/gpt-repository-loader)
*  [alisonjf - gpt3-tokenizer](https://github.com/alisonjf/gpt3-tokenizer/)
