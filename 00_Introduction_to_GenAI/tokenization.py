import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

print("Vocab Size", encoder.n_vocab) # 200019

example_text = "The cat sat on the mat"
tokens = encoder.encode(example_text)

print("Tokens => ", tokens) #[976, 9059, 10139, 402, 290, 2450]

decoded_text = encoder.decode(tokens) #The cat sat on the mat

print("Decoded Text => ", decoded_text)