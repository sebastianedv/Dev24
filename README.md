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


## Oppgave 3

### Dockerhub: 

- dockerfordevopseksamen/java-sqs-client
- SQS url: https://sqs.eu-west-1.amazonaws.com/244530008913/image-generation-queue-20

### Beskrivelse av taggestrategi:

Latest: er en kort og enkel beskrivelse av imaget, altså siste versjon. Hadde dette vært et større, reelt prosjekt, så hadde det heller blitt benyttet 1.0.0/1.1.0/2.0.0 osv for å lettere kunne skildre patches på prosjektet.


## Oppgave 5

** 1.) Automatisering og kontinuerlig levering (CI/CD)**

** 2.) Overvability(overvåkning) **

Serverløse applikasjoner har som oftest innebygde verktøy som AWS CloudWatch for logging og overvåkning. Dette funker godt for individuelle funksjoner, men kan være vanskeligere å spore hvordan dataen flyter.

I mikrotjenester så kan man bruke mer etablerte verktøy som Prometheus eller Grafana. 
Disse tilbyr med kontroll og fleksibilitet, på bekostning av at oppsettet tar mer tid og krever mer vedlikehold. 
Fordelen her, er at logging og feilsøkningsmulighetene ofte er større.


** 3.)  Skalerbarhet og kostnadskontroll **

** 4.) Eierskap og ansvar **