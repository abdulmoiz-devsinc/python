from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field, create_model
import json

# Initialize Groq LLM
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=""
)


def create_parser(schema):
    # Create a dynamic Pydantic model based on schema
    fields = {field: (str, Field(description=f"The {field} value")) for field in schema}
    DynamicModel = create_model('GeneratedData', **fields)
    parser = JsonOutputParser(pydantic_object=DynamicModel)
    return parser


def generate_data(prompt, schema):
    parser = create_parser(schema)
    # Build the JSON format example
    json_format = ", ".join(f'"{field}": "value"' for field in schema)
    json_prompt = prompt + f"\n\nRespond with ONLY valid JSON in this format: {{{json_format}}}"
    
    # Create a simple chain: HumanMessage -> LLM -> Parser
    chain = (lambda x: [HumanMessage(content=x)]) | llm | parser
    result = chain.invoke(json_prompt)
    print(json.dumps(result, indent=2))
    return result
     

