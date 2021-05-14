
FROM python:2.7.11-alpine
WORKDIR /line
EXPOSE 8080
CMD ["python3", "inwbot.py"]