FROM python:3.11.0

WORKDIR /home/

RUN echo "testing1234"

# RUN git clone https://github.com/diarlee/pragmatic.git
RUN git clone -b main --single-branch https://github.com/diarlee/pragmatic.git

WORKDIR /home/pragmatic

RUN pip install -r requirements.txt

RUN pip install mysqlclient

EXPOSE 8000

# runserver를 gunicorn command로 변경
CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pragmatic.settings.deploy && python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]