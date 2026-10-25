"""Step 1: download the symptom dataset and look at it before modeling."""
from datasets import load_dataset
import pandas as pd

ds = load_dataset("gretelai/symptom_to_diagnosis")
print(ds)  

train = ds["train"].to_pandas()
test = ds["test"].to_pandas()

train.to_csv("ml/data/train.csv", index=False)
test.to_csv("ml/data/test.csv", index=False)

print("\nColumns:", list(train.columns))
print("\nFirst 3 examples:")
print(train.head(3).to_string())

label_col = min(train.columns, key=lambda c: train[c].nunique())
text_col = [c for c in train.columns if c != label_col][0]
print(f"\nText column: '{text_col}' | Label column: '{label_col}'")

print(f"\nTrain size: {len(train)} | Test size: {len(test)}")
print(f"Number of conditions: {train[label_col].nunique()}")

print("\nExamples per condition (train):")
print(train[label_col].value_counts().to_string())

lengths = train[text_col].str.split().str.len()
print(f"\nDescription length (words): mean {lengths.mean():.0f}, min {lengths.min()}, max {lengths.max()}")