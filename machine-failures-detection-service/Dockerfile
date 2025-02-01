FROM python:3.13-slim

WORKDIR /app

COPY ["pyproject.toml", "predict.py", "xgb_clf.bin", "./"]

RUN pip install --no-cache-dir .

EXPOSE 9696

CMD ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]