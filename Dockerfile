FROM python:3.10

RUN pip install pandas scikit-learn joblib boto3

COPY train.py /opt/program/train.py

ENTRYPOINT ["python", "/opt/program/train.py"]
