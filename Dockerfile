# pull official base image
FROM python:3.10.1-slim-buster

# set working directory
WORKDIR /usr/src/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# updated
# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc libpq-dev postgresql \
  && apt-get clean

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# new
# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/backend/entrypoint.sh
RUN chmod +x /usr/src/backend/entrypoint.sh

# add app
COPY . .

# new
# run entrypoint.sh
ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]