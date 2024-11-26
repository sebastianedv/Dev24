# Readme file

* For å kontrollere bilder som er generert -> pgr301-couch-explorer/20/generate_images/*
* CloudWatch logs: log groups -> /aws/lambda/image-generator-lambda-20
* SQS-queue: -> queues -> image-generation-queue-20

For oppgave 1 & 2 så har det vært litt latskap i bildet, som har ført til litt uryddig filstruktur. Dette har ført til at app.py, generate_image.py og litt forskjellig rusk har havnet i root av prosjektet.

## Oppgave 1
# **Oppgave 1 to do - Fjerne hardkodet bucketnavn fra generate_image.py**

* HTTP endepunkt for testing av bildegenerering: https://bjocwmo11b.execute-api.eu-west-1.amazonaws.com/Prod/generate-image
Har selv brukt postman for å teste dette, funket fint for meg.

For oppgave 1, del B:
Vellykket Github workflow action som har deployet SAM-applikasjonen til AWS: 
https://github.com/sebastianedv/Dev24/actions/runs/11914764717

## Oppgave 2

For å teste sqs kø, eksempel:
- aws sqs send-message \
  --queue-url https://sqs.eu-west-1.amazonaws.com/244530008913/image-generation-queue-20 \
  --message-body "a sunset over the misty mountains, with a hint of snow"


## Oppgave 3

I oppgaven så ligger alt av filer i mappen: infra.

### Dockerhub: 

- dockerfordevopseksamen/java-sqs-client
- SQS url: https://sqs.eu-west-1.amazonaws.com/244530008913/image-generation-queue-20

### Beskrivelse av taggestrategi:

Latest: er en kort og enkel beskrivelse av imaget, altså siste versjon. Hadde dette vært et større, reelt prosjekt, så hadde det heller blitt benyttet 1.0.0/1.1.0/2.0.0 osv for å lettere kunne skildre patches på prosjektet.


## Oppgave 5

** 1.) Automatisering og kontinuerlig levering (CI/CD)**

Her har jeg dessverre ikke kommet frem til noe svar.

** 2.) Overvability(overvåkning) **

Serverløse applikasjoner har som oftest innebygde verktøy som AWS CloudWatch for logging og overvåkning. Dette funker godt for individuelle funksjoner, men kan være vanskeligere å spore hvordan dataen flyter.

I mikrotjenester så kan man bruke mer etablerte verktøy som Prometheus eller Grafana. 
Disse tilbyr med kontroll og fleksibilitet, på bekostning av at oppsettet tar mer tid og krever mer vedlikehold. 
Fordelen her, er at logging og feilsøkningsmulighetene ofte er større.


** 3.)  Skalerbarhet og kostnadskontroll **

Serverløs arkitektur skalerer automatisk etter behov og faktureres basert på bruk. Dette kan gjøre det kostnadseffektiv om man har variabel trafikk, men kan bli dyrt om man har høy trafikk eller skal skalere det mye større.

Ved bruk av mikrotjenester, så skalerer man hele tjenester. Dette kan tilby bedre kontroll og bedre for jevn trafikk. 
Verdt å merke at dette også har sine økonomiske ulemper med at man BØR ha ressurser tilgjengelig hele tiden. F.eks nattevakter som passer på at alt kjører døgnet rundt.


** 4.) Eierskap og ansvar **

I serverløs arkitektur tar skyleverandøren av seg deler av infrastrukturen når det kommer til skalering, oppdatering og tilgjengelighet.
Dette reduserer teamets ansvar, men gir mindre kontroll over produktet og fører til en avhengighet av leverandøren.

Mikrotjenester tilbyr full kontroll over infrastrukturen. Dette gir større fleksibilitet, men til gjengjeld krever mer arbeid til vedlikehold og overvåkning.