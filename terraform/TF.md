# Terraform

## Best practices
1. I added security group for my application (TCP 80) and SSH connection (TCP 22)
2. I used variables for aws access keys and keypair (Now it is required to specify the variables file for `terraform plan` and `terraform apply` with flag `-var-file`) for security reasons
3. I used different files for different types of resources
4. I used an example file for the variables


## Usage

- Copy content of the `example.tfvars` into `variables.tfvars` and change all the variables for your needs
- `terraform plan -var-file variables.tfvars`
- `terraform apply -var-file variables.tfvars`
- Now you can connect to the instance by ssh

