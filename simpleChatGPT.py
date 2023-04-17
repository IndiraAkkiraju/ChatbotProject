import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", 
                                                                            "content": "Give me 3 ideas for birthday cakes"}])
print(completion.choices[0].message.content)