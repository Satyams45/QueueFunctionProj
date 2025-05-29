import azure.functions as func
import logging

app = func.FunctionApp()

@app.function_name(name="QueueOutputFunction")
@app.route(route="add-to-queue")
@app.output_queue(queue_name="myqueue-items", connection="AzureWebJobsStorage", name="outputQueueItem")
def main(req: func.HttpRequest) -> func.QueueMessage:
    name = req.params.get("name")
    if not name:
        return func.QueueMessage("No name found")
    return func.QueueMessage(body=name)
