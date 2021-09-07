resource "aws_instance" "app_python" {
  ami             = "ami-00399ec92321828f5"
  instance_type   = "t2.micro"
  key_name        = var.key_pair_name
  security_groups = ["${aws_security_group.app_python_sg.name}"]
}