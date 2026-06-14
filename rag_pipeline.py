#your rag_pipeline.py becomes the orchestrator:
from fetching import fetch
from Generator import generate

print("\nWhat you are looking for?\n")
while True:
    
    user_input=input("🧑: ")

    #calling fetch function(def fetch(qry:str,k=k)
    docs=fetch(user_input) #query = "What caused the payment service timeout?"
    context=context = "\n\n\n".join([
    f"Page Content: {doc.page_content}\n"
    f"Page Number: {doc.metadata['page_label']}\n"
    f"File Location: {doc.metadata['source']}"
    for doc in docs 
    
])
    print("\n========== RETRIEVING CONTEXT FOR YOU==========\n")
    ans=generate(context,user_input) #generate() returns a Pydantic object
    
    
    print("\n🤖: Incident Details:\n")
    #model_dump_json() is a Pydantic method that converts a Pydantic object into a JSON string
    print(f"""
    Incident Id: {ans.incident_id},
    Service: {ans.service}
    Severity: {ans.severity}
    Date: {ans.date}
    Summary: {ans.summary}
    Impact: {ans.impact}
    Root Cause: {ans.root_cause}
    Resolution: {ans.resolution}
    Page Number: {ans.page_number}
    Prevention_Actions: {ans.prevention_actions}
""")
    