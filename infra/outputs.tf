output "sqs_queue_url" {
  description = "URL of the SQS queue"
  value       = aws_sqs_queue.image_queue.id
}

output "lambda_function_name" {
  description = "Name of the Lambda function"
  value       = aws_lambda_function.image_generator_lambda_20.function_name
}