CRM_system
docker compose run --rm app sh

Якщо дамп знаходиться на хості (ззовні контейнера), спочатку потрібно скопіювати його всередину контейнера за допомогою:
docker cp ~/Downloads/your_dump_file.sql app:/your_dump_file.sql

Перевір, чи файл скопіювався:
docker exec -it app sh

Потім перевір, чи файл є у контейнері:
ls -l /

Імпортувати дамп у хмарну базу даних: 
mysql -u username -p -h your-database-host.com -P 3306 database_name < /path/to/dump.sql
