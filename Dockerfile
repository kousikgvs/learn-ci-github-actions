FROM python:3.12-slim

WORKDIR /app

COPY add_numbers.py /app/add_numbers.py

ENTRYPOINT ["python", "add_numbers.py"]
CMD ["--a", "2", "--b", "3"]
