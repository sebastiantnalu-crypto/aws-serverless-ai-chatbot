# AWS Serverless AI Chatbot

A cloud-native serverless chatbot built using AWS services and DevOps practices.  
The project demonstrates how to design scalable cloud applications using serverless architecture, infrastructure as code, and CI/CD automation.

## Architecture

User → API Gateway → AWS Lambda → DynamoDB → Response

The system processes user messages via a REST API and generates responses using a Python-based backend deployed on AWS Lambda.

## Features

- Serverless architecture using AWS Lambda
- REST API integration
- Chat history storage in DynamoDB
- Infrastructure provisioning using Terraform
- Automated deployment using GitHub Actions
- Monitoring using AWS CloudWatch

## Technologies Used

- AWS Lambda
- AWS API Gateway
- AWS DynamoDB
- Terraform
- GitHub Actions (CI/CD)
- Python
- REST APIs
- Git & GitHub

## Deployment

1. Clone the repository
git clone https://github.com/yourusername/aws-serverless-ai-chatbot.git

2. Configure AWS credentials
aws configure

3. Initialize Terraform
terraform init

4. Deploy infrastructure
terraform apply

The CI/CD pipeline automatically deploys updates when code is pushed to the main branch.

## Future Improvements

- Integrate OpenAI API for advanced conversational responses
- Add frontend chatbot interface hosted on AWS S3
- Implement authentication using AWS Cognito

  
What This Shows Recruiters

This project demonstrates:
AWS,
Serverless architecture,
Terraform (Infrastructure as Code),
CI/CD pipelines,
Python backend,
Cloud automation, and
DevOps practices
