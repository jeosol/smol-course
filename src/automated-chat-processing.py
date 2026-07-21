from transformers import pipeline

# Initialize the pipeline
# SmolLM3-3B-Base is the Base model trained on raw test to predict next token.
# SmolLM3-3B is Instruct Model fine-tuned to follow instructions
# Link to the model: https://huggingface.co/HuggingFaceTB/SmolLM3-3B

pipe = pipeline("text-generation", "HuggingFaceTB/SmolLM3-3B", device_map="auto")

# Define your conversation
messages = [
        {"role": "system", "content": "You are a friendly chatbot who always responds in the style of a pirate"},
            {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
            ]

# Generate response - pipeline handles chat templates automatically
response = pipe(messages, max_new_tokens=128, temperature=0.7)
print(response[0]['generated_text'][-1])  # Print the assistant's response
