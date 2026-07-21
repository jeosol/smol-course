from transformers import pipeline

pipe = pipeline("text-generation", "HuggingFaceTB/SmolLM3-3B", device_map="auto")

# Define your conversation
messages = [
        {"role": "system", "content": "You are a friendly chatbot who always responds in the style of a pirate"},
        {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
]

# Configure generation parameters
generation_config = {
 "max_new_tokens": 200,
 "temperature": 0.8,
 "do_sample": True,
 "top_p": 0.9,
 "repetition_penalty": 1.1
 }

# Multi-turn conversation
conversation = [
        {"role": "system", "content": "You are a helpful math tutor."},
        {"role": "user", "content": "Can you help me with calculus?"},
]

# Generate first response
response = pipe(conversation, **generation_config)
conversation = response[0]['generated_text']

# Continue the conversation
conversation.append({"role": "user", "content": "What is a derivative?"})
response = pipe(conversation, **generation_config)

print("Final conversation:")
for message in response[0]['generated_text']:
        print(f"{message['role']}: {message['content']}")
