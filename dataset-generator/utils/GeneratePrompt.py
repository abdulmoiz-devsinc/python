
def generate_prompt(dataframe, schema):

    for row in dataframe.itertuples(index=False):
        row_data = ", ".join(f"{col}={getattr(row, col)}" for col in dataframe.columns)
        prompt = f"Given the schema:\n{schema}\nGenerate data for the following row:\n{row_data}\n"
        yield prompt
