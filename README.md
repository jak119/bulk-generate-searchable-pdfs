# PDF OCR Processing Tool

## Overview
This project provides a Python script for converting PDF files to searchable PDFs using Azure Document Intelligence (formerly Form Recognizer) with infrastructure managed by Terraform.

## Features
- Batch process PDF files in a specified input folder
- Convert PDFs to searchable format using Azure Document Intelligence
- Terraform-managed Azure Cognitive Services infrastructure

## Prerequisites
- Python 3.x
- Azure Subscription
- Terraform (version >= 1.10)

## Infrastructure Setup
The Terraform configuration (`main.tf`) creates:
- A resource group in East US 2 region
- An Azure Cognitive Account for Document Intelligence
- Uses Azure/naming module for consistent resource naming
- Configures a Form Recognizer service with S0 SKU

### Providers
- Azure Resource Manager (azurerm)

### Configuration and Deployment
1. Set up Azure credentials
2. Initialize Terraform:
```bash
terraform init
```

3. Review and apply Terraform configuration:
```bash
terraform plan
terraform apply
```

4. Retrieve the endpoint and key outputs for below
```bash
# Get all outputs
terraform output

# Get key since it's marked sensitive
terraform output key
```

## Python Script Usage
1. Create a `.env` file as below
```
ENDPOINT=<endpoint from terraform>
KEY=<key from terraform>
```

2. Set input and output folder paths in the script
3. Run the Python script:
```bash
python generate_searchable_pdfs.py
```
