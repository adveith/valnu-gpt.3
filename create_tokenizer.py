# create_tokenizer.py

import pickle
from tensorflow.keras.preprocessing.text import Tokenizer

def save_tokenizer(texts, file_path):
    """
    Tokenizes input texts and saves the tokenizer to a pickle file.

    Args:
    - texts (list of str): Input texts to tokenize and fit the tokenizer.
    - file_path (str): File path to save the tokenizer pickle file.

    Returns:
    - None
    """
    try:
        # Initialize the tokenizer
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(texts)

        # Save the tokenizer to a file
        with open(file_path, 'wb') as handle:
            pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

        print(f"Tokenizer has been saved to {file_path}")

    except FileNotFoundError as e:
        print(f"Error: The directory for the file '{file_path}' does not exist.")
    except IOError as e:
        print(f"Error: Failed to write to the file '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred while saving the tokenizer: {str(e)}")

# Example input data
texts = [
    "How to fix CWE-79?",
    "Tell me about CWE-89.",
    "What are the mitigations for CWE-22?",
    "Describe CWE-502."
]

# File path to save the tokenizer
tokenizer_file = 'models/tokenizer.pickle'

# Save the tokenizer with enhanced error handling
save_tokenizer(texts, tokenizer_file)
