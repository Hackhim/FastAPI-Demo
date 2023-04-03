FROM python:3.10

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pdm

COPY pyproject.toml pdm.lock /app/

RUN pdm export > requirements.txt
RUN pip install -r requirements.txt

COPY main.py /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]