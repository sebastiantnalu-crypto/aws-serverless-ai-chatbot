provider "aws" {
  region = "eu-north-1"
}

resource "aws_dynamodb_table" "chat_table" {
  name         = "ChatHistory"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

resource "aws_lambda_function" "chatbot_lambda" {
  function_name = "chatbot_lambda"

  filename      = "../../lambda/chatbot.zip"
  handler       = "chatbot.lambda_handler"
  runtime       = "python3.10"
  role          = aws_iam_role.lambda_role.arn
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda_chatbot_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
      Effect = "Allow"
    }]
  })
}
