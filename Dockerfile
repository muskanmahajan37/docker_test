FROM python:3.7
COPY . /app
WORKDIR /app
RUN python3 -m pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["flask_app.py"]