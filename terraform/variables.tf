variable "aws_access_key_id" {
  type        = string
  description = "AWS account access key id"
}

variable "aws_secret_access_key" {
  type    = string
  default = "AWS account secret access key"
}

variable "key_pair_name" {
  type    = string
  default = "AWS key pair for the instance"
}