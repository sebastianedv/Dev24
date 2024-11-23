# Readme file

* For å kontrollere bilder som er generert -> pgr301-couch-explorer/20/generate_images/*
* CloudWatch logs: log groups -> /aws/lambda/image-generator-lambda-20
* SQS-queue: -> queues -> image-generation-queue-20

## Oppgave 1
Oppgave 1 to do - Fjerne hardkodet bucketnavn fra generate_image.py

* HTTP endepunkt for testing av bildegenerering: https://bjocwmo11b.execute-api.eu-west-1.amazonaws.com/Prod/generate-image
Har selv brukt postman for å teste dette, funket fint for meg.

For oppgave 1, del B:
Vellykket Github workflow action som har deployet SAM-applikasjonen til AWS: 
https://github.com/sebastianedv/Dev24/actions/runs/11914764717

## Oppgave 2

* husk:
* cd intra -> terraform init -> terraform apply

For å teste sqs kø, eksempel:
- aws sqs send-message \
  --queue-url https://sqs.eu-west-1.amazonaws.com/244530008913/image-generation-queue-20 \
  --message-body "a sunset over the misty mountains, with a hint of snow"
