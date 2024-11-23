# Readme file

For å kontrollere bilder som er generert -> pgr301-couch-explorer/20/generate_images/*
CloudWatch logs: log groups -> /aws/lambda/image-generator-lambda-20
SQS-queue: -> queues -> image-generation-queue-20

## Oppgave 1
Oppgave 1 to do - Fjerne hardkodet bucketnavn fra generate_image.py

* HTTP endepunkt for testing av bildegenerering: https://bjocwmo11b.execute-api.eu-west-1.amazonaws.com/Prod/generate-image
Har selv brukt postman for å teste dette, funket fint for meg.

For oppgave 1, del B:
Vellykket Github workflow action som har deployet SAM-applikasjonen til AWS: 
https://github.com/sebastianedv/Dev24/actions/runs/11914764717

Oppgave 2
