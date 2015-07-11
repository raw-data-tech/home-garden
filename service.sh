git pull
service nginx restart
pkill gunicorn
gunicorn -w3  apps.wsgi --bind 127.0.0.1:8000  &


