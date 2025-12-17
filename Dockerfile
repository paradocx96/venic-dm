FROM python:3.7.7-stretch AS BASE

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
    build-essential \
    curl \
    git \
    jq \
    libgomp1 \
    vim

WORKDIR /app

# upgrade pip version
RUN pip install --no-cache-dir --upgrade pip
RUN pip install rasa==3.0.8

COPY . .

EXPOSE 5005

CMD ["rasa", "run", "--enable-api","-p", "5005", "--cors", "*", "--debug"]
