FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /gudangObatv2
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8000
CMD exec gunicorn gudangObatv2.wsgi:application –bind 0.0.0.0:8000 –workers 3