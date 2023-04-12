FROM django:4.2
EXPOSE 8000
WORKDIR .
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "makemigrations", "migrate"]
