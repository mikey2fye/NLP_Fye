from openai import OpenAI
import os
import pandas as pd
import csv
import json

def parse_reviews(file):
  df = pd.read_csv(file)
  count = 1
  for review in df:
    if count < 6:
      prompt = f"Given the followingt review for a restaurant: {review}. What is the sentiment of this review?"
      response = client.completions.create(model = "gpt-3.5-turbo", 
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 100
    )
    count += 1
  return response.choices[0].text.strip()

client = OpenAI(api_key = "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")

# print(df.to_string())
md = pd.read_csv("four_star_reviews_sample.csv")
# print(md.to_string())

print(parse_reviews("one_star_reviews_sample.csv"))