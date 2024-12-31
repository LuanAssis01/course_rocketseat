import ollama 

client = ollama.Client()

context = """ Voce é um assistente pessoal """

instruction = """ Olá. Como voce está? """

prompt = f"Context: {context}\n\nQuestion: {instruction}"

response = client.generate(model="llama3.2", prompt=prompt)

print("Resposta do Llama:", response['response'])