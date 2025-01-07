module "naming" {
  source = "Azure/naming/azurerm"
  suffix = ["ocr"]
}

resource "azurerm_resource_group" "ocr" {
  name     = module.naming.resource_group.name
  location = "East US 2"
}

resource "azurerm_cognitive_account" "ocr" {
  name                = module.naming.cognitive_account.name_unique
  location            = azurerm_resource_group.ocr.location
  resource_group_name = azurerm_resource_group.ocr.name
  kind                = "FormRecognizer"

  sku_name = "S0"
}

output "key" {
  value     = azurerm_cognitive_account.ocr.primary_access_key
  sensitive = true
}
