# ErikWeb Django on Azure with Terraform

This project deploys a Django application to Azure using Terraform, with Azure App Service and PostgreSQL, utilizing a managed identity.

## Prerequisites

- Azure CLI installed and logged in (`az login`)
- Terraform installed (v1.0+)
- Python 3.9+

## Setup

1. Clone or navigate to the project directory.

2. Copy `terraform.tfvars.example` to `terraform.tfvars` and fill in the required values:

   ```bash
   cp terraform.tfvars.example terraform.tfvars
   ```

   Edit `terraform.tfvars` with your desired values, especially:
   - `postgres_admin_password`: A strong password for the PostgreSQL admin
   - `django_secret_key`: A secure secret key for Django

3. Initialize Terraform:

   ```bash
   terraform init
   ```

4. Plan the deployment:

   ```bash
   terraform plan
   ```

5. Apply the changes:

   ```bash
   terraform apply
   ```

   Confirm with `yes` when prompted.

## Deployment

After Terraform applies, the infrastructure is ready. To deploy the Django code:

1. The Web App is configured to deploy from source. You can use Azure CLI to deploy:

   ```bash
   az webapp up --name <web_app_name> --resource-group <resource_group_name> --runtime PYTHON:3.9
   ```

   Or set up CI/CD with GitHub Actions.

2. Azure App Service will automatically:
   - Install dependencies from `requirements.txt`
   - Run `python manage.py collectstatic`
   - Run `python manage.py migrate`
   - Start the Gunicorn server

## Managed Identity

The Azure Web App has a system-assigned managed identity enabled. You can use this identity to access other Azure resources securely.

For example, to grant access to Azure Key Vault or other services, use the principal ID from the Terraform output.

## Outputs

After deployment, Terraform will output:
- `web_app_url`: The URL of your deployed app
- `postgres_server_fqdn`: The PostgreSQL server FQDN
- `web_app_identity_principal_id`: The managed identity principal ID

## Local Development

For local development, ensure you have the environment variables set as in `settings.py`.

You can run locally with:

```bash
pip install -r requirements.txt
python manage.py runserver
```

## Security Notes

- Change the default passwords and secret keys.
- In production, consider using Azure Key Vault for secrets.
- The PostgreSQL server is configured with basic settings; adjust for production needs.