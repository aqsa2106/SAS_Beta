# Contoh skrip Terraform untuk pengujian
resource "aws_s3_bucket" "b" {
  bucket = "my-tf-test-bucket"
}
