
FROM python:2.7.11-alpine
ADD ./web /opt/web/
WORKDIR /opt/web
EXPOSE 8080
CMD ["python3", "inwbot.py"]