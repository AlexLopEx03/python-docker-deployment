FROM python:3.11-slim

COPY main.py .

EXPOSE 8080

CMD ["python", "main.py"]
