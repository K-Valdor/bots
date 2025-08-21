# DECISIONS
- Docker+Compose; общий кластер Postgres; изоляция по схемам/ролям.
- Профиль БД: 2GB (max_connections=40, shared_buffers=256MB, work_mem=4MB).
- Бэкапы: pre-release dump; weekly cron — опционально; retention 7–14d.
- Релизы/откаты: теги vX.Y.Z, миграции обратимые или pre-release dump.
- Секреты: GitHub Secrets (деплой), env-файлы на VPS (токены ботов).
