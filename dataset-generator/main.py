from utils.ReadUserDataset import read_user_dataset
from utils.readSchema import read_schema_file
from utils.GeneratePrompt import generate_prompt
from utils.GenerateData import generate_data
import pandas as pd

path=input("Enter the path to the dataset file: ")
df=read_user_dataset(path)

print("Dataset Dimensions: ",df.shape)
print("DataSet preview: \n", df.head())

text_file_path=input("Enter schema file path: ")
schema=read_schema_file(text_file_path)
print("Schema Content: \n", schema)

generated_rows = []

for idx, prompt in enumerate(generate_prompt(df, schema)):
    generated_data = generate_data(prompt, schema)
    print("Generated Data: \n", generated_data)
    generated_rows.append(generated_data)

generated_df = pd.DataFrame(generated_rows)

combined_df = pd.concat([df.reset_index(drop=True), generated_df.reset_index(drop=True)], axis=1)

print("\nCombined Dataset: \n", combined_df)


output_path = path.replace('.csv', '_new.csv')
combined_df.to_csv(output_path, index=False)
print(f"\nData saved to {output_path}")

    
