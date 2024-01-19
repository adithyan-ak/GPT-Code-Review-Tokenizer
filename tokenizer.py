import yaml
from transformers import GPT2Tokenizer
import gpt3_tokenizer

def count_tokens(text: str) -> int:
    return gpt3_tokenizer.count_tokens(text)

def tokenize_line(line: str, tokenizer) -> list:
    return tokenizer.encode(line, add_special_tokens=False)

def write_chunk_to_file(chunk_tokens: list, chunk_id: int, tokenizer, output_file_pattern: str) -> None:
    chunk_name = output_file_pattern.format(chunk_id=chunk_id)
    with open(chunk_name, 'w', encoding='utf-8') as chunk_file:
        decoded_text = tokenizer.decode(chunk_tokens)
        chunk_file.write(decoded_text)

        token_count = count_tokens(decoded_text)
        if token_count is not None:
            print(f"Chunk {chunk_id} Token Count: {token_count}")
        else:
            print(f"Chunk {chunk_id} Token Count: Could not be determined.")

def split_file_into_chunks(config: dict) -> None:
    try:
        tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        filename = config['input_file_name']
        max_tokens = config['max_tokens']
        output_file_pattern = config['output_file_pattern']

        current_chunk_id = 1
        current_chunk_tokens = []

        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line_tokens = tokenize_line(line, tokenizer)
                
                # Check if adding this line exceeds the max token limit
                if len(current_chunk_tokens) + len(line_tokens) > max_tokens:
                    if current_chunk_tokens:  # Write non-empty chunk to file
                        write_chunk_to_file(current_chunk_tokens, current_chunk_id, tokenizer, output_file_pattern)
                        current_chunk_id += 1
                    current_chunk_tokens = line_tokens  # Start new chunk
                else:
                    current_chunk_tokens.extend(line_tokens)

        # Write the last chunk if it has content
        if current_chunk_tokens:
            write_chunk_to_file(current_chunk_tokens, current_chunk_id, tokenizer, output_file_pattern)

        print(f"File '{filename}' split into {current_chunk_id} chunks.")
    except Exception as e:
        print(f"An error occurred: {e}")

def load_config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config()['tokenizer_config']
    split_file_into_chunks(config)

if __name__ == "__main__":
    main()
