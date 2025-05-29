# Azure Function: Storage Queue & SQL Output Binding (Python)

**Name:** Satyam Panseriya 
**Student ID:** 041128392  
**Email:** pans0012@algonquinlive.com  

## Video Demonstrations

- [Part 1 - Queue Binding Demo]()  
- [Part 2 - SQL Binding Demo]()

---

## Project Overview

In this lab, we develop two serverless Azure Function apps using Python and Visual Studio Code. We implement output bindings to connect your functions with Azure Storage Queues and Azure SQL Database.

---

## Tasks 

### 1. Storage Queue Output Binding
- Complete all steps from the Storage Queue output binding QuickStart.
- Use Python as your programming language and VS Code as your development environment.
- Test the function locally and deploy it to Azure.
- Confirm that queue messages are added correctly when the function is triggered.

### 2. Azure SQL Output Binding
- Complete all steps from the Azure SQL output binding QuickStart.
- Again, use Python and VS Code.
- Make sure to set up the Azure SQL Database and table schema as instructed.
- Verify that your function inserts records into the database successfully.

  
---


### 💻 Local Environment Requirements

- Python 3.8 or 3.9
- Azure Functions Core Tools
- Visual Studio Code with extensions:
  - Python
  - Azure Functions
  - Azure Storage
- Azure Storage Explorer
- (Optional) Azurite for local queue emulation

---

## Queue Output Binding

### Function Code (`function_app.py`)
```python
import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="QueueOutputFunction", auth_level=func.AuthLevel.ANONYMOUS)
def QueueOutputFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
  ```

## Register Binding Extensions

To ensure proper functionality of Azure Function bindings, update the `host.json` file with the appropriate extension bundle configuration depending on the binding type.

### Queue Binding

For Azure Storage Queue binding support, include the following in your `host.json`:

```json
{
  "version": "2.0",
  "logging": {
    "applicationInsights": {
      "samplingSettings": {
        "isEnabled": true,
        "excludedTypes": "Request"
      }
    }
  },
  "extensionBundle": {
    "id": "Microsoft.Azure.Functions.ExtensionBundle",
    "version": "[4.*, 5.0.0)"
  }
}
```
### SQL Binding
For Azure SQL binding support, use the following host.json configuration:

  ```json
{
  "version": "2.0",
  "extensionBundle": {
    "id": "Microsoft.Azure.Functions.ExtensionBundle",
    "version": "[4.*, 5.0.0)"
  }
}
```
# Azure Function App – Run, Test, and Deploy Guide

## Run & Test

### 1. Run Locally

- Press `F5` in Visual Studio Code to start the function app locally.

### 2. Execute the Function

- In the **Azure Functions** project, right-click on `HttpExample` → **Execute Function Now**.
- Provide the following test input:
`{
  "name": "Azure"
}`

## Deploy

 - F1 → Azure Functions: Deploy to Function App

------

#  SQL Output Binding
