from openai import OpenAI
import os
from dotenv import load_dotenv
import json
from schemas import Incidents

load_dotenv()

# Keep this! The Gemini LLM needs it to generate the final response.
llm=OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"

)

def generate(context: str, query:str):

    system_prompt = f"""
You are an Incident Management Assistant.
IMPORTANT:
- Return ONLY valid JSON.
- Do NOT return markdown.
- Do NOT return text outside the JSON object.
- Your response must start with {{ and end with }}.
- If the user asks for a specific field (root cause, resolution, severity, impact, etc.), return only that information.
- If the user asks for full incident details, return:
{{
  "incident_id":"",
  "service":"",
  "severity":"",
  "date":"",
  "summary":"",
  "impact":"",
  "detection":"",
  "root_cause":"",
  "resolution":"",
  "page_number":"",
  "prevention_actions":""
}}

If multiple incidents match, return the most relevant one.
If an incident is identified, return all fields

If no incident is found:

{{
  "error":"Incident not found"
}}

User Question:
{query}

Context:
{context}
"""

    ai_response=llm.chat.completions.create(
    messages=[
        {"role":"system","content":system_prompt},
        {"role":"user","content":query}
    ],
    model="gemini-2.5-flash"
)
    
    return_resp= ai_response.choices[0].message.content    
    # Remove markdown fences
    return_resp = return_resp.replace("```json", "")
    return_resp = return_resp.replace("```", "")
    return_resp = return_resp.strip()
    data=json.loads(return_resp)
    incident=Incidents(**data) #Convert dict → Pydantic object:
    return incident

#The LLM returns a plain string — not a Python object.
# Even though you asked it to return JSON, what actually comes back is just text that looks like JSON:return_resp = '{"incident_id": "INC001", "service": "payment", "severity": "high", ...}'
# This is just a STRING, not a Python dict

#json.loads() converts that string → Python dict
#Then Pydantic takes the dict → typed object

#Why not skip json.loads() and pass the string directly to Pydantic? Because Pydantic expects a dict (**data), not a raw string. You need json.loads() as the bridge between the two.

#data = {"incident_id": "INC001", "service": "payment", "severity": "high"}Incidents(**data)
# is exactly the same as writing:
# Incidents(incident_id="INC001", service="payment", severity="high")
  

#The user input is captured in rag_pipeline.py and passed as an argument to generation.py. That's why generation.py doesn't need its own input() call. This separation makes the code reusable later for FastAPI, Streamlit, or LangGraph.