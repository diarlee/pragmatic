FROM python:3.11.0

WORKDIR /home/

RUN git clone https://github.com/diarlee/pragmatic.git

WORKDIR /home/pragmatic

Run pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-q2uh5rt1(kwlai%5ezh3rc71w1rqp_k$&^uvm22!f)^!taf$=w" > .env

Run python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]