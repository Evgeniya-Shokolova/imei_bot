# IMEI Проверка Telegram Бот

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=anuraghazra&layout=compact)](https://github.com/anuraghazra/github-readme-stats)

### Описание

Данный бот позволяет пользователям проверять правильность IMEI-номеров и получать информацию о мобильных устройствах. Просто отправьте IMEI-номер боту, и он вернет вам результаты проверки.



Выполнить клонирование
```bash
git clone git@github.com: imei_bot.git
```
Перейти в папку с проектом
```bash
cd imei_bot
```
Создать виртуальное окружение:
   Команда для Windows: -
```bash
python -m venv venv
```
Команда для Linux и macOS: - 
```bash
python3 -m venv venv
```
Активировать виртуальное окружение:`
   Команда для Windows: -
```bash
source venv/Scripts/activate
```
Для Linux и macOS: -
```bash
source venv/bin/activate
```
Обновить пакетный менеджер:
   Для Windows: -
```bash
python -m pip install --upgrade pip
```
Для Linux и macOS: -
```bash
python3 -m pip install --upgrade pip
```
Установить модули из файла requirementst.txt:`
```bash
pip install -r requirements.txt
```
Запустить бота
```bash
uvicorn main:app --reload
```

## Сохраняем, коммитим и пушим изменения на GitHub
```bash
git add .
```
```bash
git commit -m "Comment"
```
```bash
git push
```

### Автор:
[Евгения Шоколова](https://github.com/Evgeniya-Shokolova)
