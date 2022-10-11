FROM python:3.9

# Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app","--workers", "2" ,"--host", "0.0.0.0", "--port", "5001"]