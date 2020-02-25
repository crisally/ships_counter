FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8
RUN adduser -D ship_counter
WORKDIR /home/ship_counter
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY main.py ./
RUN chown -R ship_counter:ship_counter ./
USER ship_counter
CMD uvicorn main:app --host 0.0.0.0 --port 8000