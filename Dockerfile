FROM python:3.9-slim-bullseye
ENV PYTHONUNBUFFERED 1

WORKDIR /app
EXPOSE 80

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt
RUN pip install torch==1.12.1+cpu torchvision==0.13.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
COPY . .
CMD python manage.py runserver 0.0.0.0:80
