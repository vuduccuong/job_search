FROM python:3.11

WORKDIR /job_app

COPY requirements/base.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "src/main:app", "--host", "0.0.0.0", "--port", "8000"]