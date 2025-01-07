import os
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeOutputOption, AnalyzeResult
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

# Azure configuration
endpoint = os.getenv('ENDPOINT')
api_key = os.getenv('KEY')

# Directory paths
input_folder = "source"
output_folder = "output"

# Initialize the client
document_intelligence_client = DocumentIntelligenceClient(
    endpoint=endpoint, 
    credential=AzureKeyCredential(api_key), 
    # api_version='2024_11_30'
)

# Function to process PDFs
def process_pdfs(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, f"searchable_{filename}")

            print(f"Processing: {filename}")

            with open(input_file_path, "rb") as f:
                # Start the "read" operation
                poller = document_intelligence_client.begin_analyze_document(
                    "prebuilt-read",
                    body=f,
                    output=[AnalyzeOutputOption.PDF],
                )
            result: AnalyzeResult = poller.result()
            operation_id = poller.details["operation_id"]

            response = document_intelligence_client.get_analyze_result_pdf(model_id=result.model_id, result_id=operation_id)
            with open(output_file_path, "wb") as writer:
                writer.writelines(response)

if __name__ == "__main__":
    process_pdfs(input_folder, output_folder)
