FROM public.ecr.aws/docker/library/python:3.10

WORKDIR /app

COPY ..

RUN pip install pandas scikit-learn joblib boto3

ENTRYPOINT ["python", "/opt/program/train.py"]
