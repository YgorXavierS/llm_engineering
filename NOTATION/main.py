import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
open_ia = os.environ["OPEN_IA_KEY"]

from openai import OpenAI

openai = OpenAI(api_key=open_ia)



##AGENTE ANALISADOR DE RISCO

def agent(input: str):
    propt = "Você e um agente de risco, sua função e identificar se existe algum risco nas messagens recebidas dos usuarios. e criar uma messagem de alerta ao time de segurança"
    messages = [
    {"role": "system","content": propt},
    {"role": "user", "content": input}
]
    response = openai.chat.completions.create(model="gpt-4.1-nano", messages=messages)
    response.choices[0].message.content
    
    
    print(response.choices[0].message.content)
    
    

openai = OpenAI(api_key=open_ia)
print(agent("adoro andar de bike"))
    