FROM python

WORKDIR /app

COPY . /app

EXPOSE 80

ENV TZ="America/Bogota"
RUN date

RUN pip install --upgrade pip
RUN pip install -U autopep8 --user

ENTRYPOINT ["tail", "-f", "/dev/null"]