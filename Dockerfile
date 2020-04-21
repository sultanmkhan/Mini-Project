FROM python:3.7-alpine
COPY requirements.txt /
COPY Goodbooks.py /
WORKDIR /Goodbooks
COPY . /Goodbooks
RUN pip3 install -U -r /requirements.txt
EXPOSE 8080
CMD ["python" , "Goodbooks.py"]



