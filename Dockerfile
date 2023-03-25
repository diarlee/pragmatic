FROM python:3.11.0

WORKDIR /home/

RUN git clone https://github.com/diarlee/pragmatic.git

WORKDIR /home/pragmatic

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-q2uh5rt1(kwlai%5ezh3rc71w1rqp_k$&^uvm22!f)^!taf$=w" > .env

RUN  python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]