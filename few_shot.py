from openai import OpenAI
import os


client = OpenAI()

# def zeroShot(file):
#     s = []
#     with open(file, "r") as f:
#         for line in f.readlines():
#             s.append(line)
#     prompt = f"Given the following review for a restaurant: {s[0]}. What is the sentiment of this review?"
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant with extensive experience in data science and technical writing."},
#             {"role": "user", "content": prompt}
#     ]
# )
#     # response = client.completions.create(model = "gpt-3.5-turbo", 
#     #     prompt = prompt,
#     #     temperature = 0.5,
#     #     max_tokens = 100
#     # )
#     return completion.choices[0].message

# print(zeroShot("GoT_hilight1.txt"))


response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Summarize what happened during this scene? "
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)