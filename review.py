from openai import OpenAI
import pandas as pd

# client = OpenAI(
#   organization='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',
# )

df = pd.read_csv("one_star_reviews_sample.csv")
print(df.to_string())
md = pd.read_csv("four_star_reviews_sample.csv")
print(md.to_string())
