CRM_system
docker compose run --rm app sh

Якщо дамп знаходиться на хості (ззовні контейнера), спочатку потрібно скопіювати його всередину контейнера за допомогою:
docker cp /path/to/your/dump.sql <container_name_or_id>:/path/in/container/dump.sql

Імпортувати дамп у хмарну базу даних: 
mysql -u username -p -h your-database-host.com -P 3306 database_name < /path/to/dump.sql
