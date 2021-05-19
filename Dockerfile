FROM python:3.8-alpine
WORKDIR /sarogya-aetu
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "-m","pytest","-vv"]
