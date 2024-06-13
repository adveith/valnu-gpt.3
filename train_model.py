import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
import pickle

# Example data (replace with your actual dataset)
sentences = [
    'How to fix CWE-79?',
    'Tell me about CWE-89.',
    'What are the mitigations for CWE-22?',
    'Describe CWE-502.',
    # Add more examples as needed
]
labels = [0, 1, 2, 3]  # Example labels for intents

def train_intent_classifier(sentences, labels, tokenizer_file='models/tokenizer.pickle', model_file='models/intent_model.h5'):
    # Initialize and fit the tokenizer
    tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
    tokenizer.fit_on_texts(sentences)

    # Save the tokenizer for later use
    with open(tokenizer_file, 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # Convert sentences to sequences and pad them
    sequences = tokenizer.texts_to_sequences(sentences)
    padded_sequences = pad_sequences(sequences, maxlen=20, padding='post', truncating='post')

    # Convert labels to numpy array
    labels = np.array(labels)

    # Define the model
    model = Sequential([
        Embedding(input_dim=10000, output_dim=64, input_length=20),
        Bidirectional(LSTM(64)),
        Dense(64, activation='relu'),
        Dense(len(set(labels)), activation='softmax')  # Adjust output layer based on number of unique intents
    ])

    # Compile the model
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train the model
    model.fit(padded_sequences, labels, epochs=10)

    # Save the model
    model.save(model_file)

    print(f"Model and tokenizer have been saved to {model_file} and {tokenizer_file}.")

if __name__ == "__main__":
    train_intent_classifier(sentences, labels)
