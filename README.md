# Project-C

Database openen
1. Ga naar de map waar het bestand manage.py is opgeslagen: in mijn geval C:\Users\Suzan\Desktop\Project-C\Django\website.
2. Zorg ervoor dat niets geselecteerd is en klik bij het menu(bovenin) op 'Bestand' --> 'Windows Powershell openen' --> 'Windows Powershell openen als admin'
3. Als dit de 1e keer is dat je deze database op je huidige computer in Django opent:
   Typ in: py manage.py createsuperuser
   username: admin
   email: random email, bijv admin@admin.com
   password: admin
   password (again): admin
4. Typ in: py manage.py runserver
5. Ga naar http://127.0.0.1:8000/admin om de database te bekijken en bestanden in de database te zetten

Nieuwe tabellen maken
1. Ga naar Project-C\Django\website\art in de map waar je de Git repository hebt opgeslagen
2. Open models.py in je IDE (ik gebruik Visual Studio Code, maar je bent vrij in de keuze)
3. Om een tabel toe te voegen aan de database moet je er een model voor maken, dat doe je in models.py
4. Nadat je het model hebt gemaakt, open je admin.py
5. Daar voeg je het model toe aan het admin paneel op dezelfde manier als het model Painting
6. Open Windows Powershell in de map waar manage.py zit
7. Typ in: manage.py makemigrations
8. Typ in: manage.py migrate
9. Typ in: manage.py runserver en ga naar http://127.0.0.1:8000/admin om items in de tabellen te zetten
