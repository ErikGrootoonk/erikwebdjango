variable "resource_group_name" {
  description = "Name of the Azure resource group"
  type        = string
  default     = "erikweb-rg"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "West Europe"
}

variable "postgres_server_name" {
  description = "Name of the PostgreSQL server"
  type        = string
  default     = "erikweb-postgres"
}

variable "postgres_admin_username" {
  description = "Admin username for PostgreSQL"
  type        = string
  default     = "postgresadmin"
}

variable "postgres_admin_password" {
  description = "Admin password for PostgreSQL"
  type        = string
  sensitive   = true
}

variable "database_name" {
  description = "Name of the database"
  type        = string
  default     = "erikwebdb"
}

variable "app_service_plan_name" {
  description = "Name of the App Service Plan"
  type        = string
  default     = "erikweb-plan"
}

variable "web_app_name" {
  description = "Name of the Web App"
  type        = string
  default     = "erikweb-app"
}

variable "django_secret_key" {
  description = "Django secret key"
  type        = string
  sensitive   = true
}

variable "allowed_hosts" {
  description = "Allowed hosts for Django"
  type        = string
  default     = "erikweb-app.azurewebsites.net"
}