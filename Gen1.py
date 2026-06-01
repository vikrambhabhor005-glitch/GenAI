from openai import OpenAI

api_key = "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"

client=OpenAI(
    api_key=api_key
)
response = client.responses.create(
    model="gpt-3.5-turbo",
    instructions="Act as my helpful assistant",
    input="What is capital of france",
)
print(response.output_text)

