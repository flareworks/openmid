FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

ENTRYPOINT ["/code/docker-entrypoint.sh"]

# Set git to auto convert line endings.
RUN git config --global core.autocrlf true