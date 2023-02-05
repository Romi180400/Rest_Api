FROM python:3.7-alpine
WORKDIR /REST_API
COPY Backend_testing.py rest_server.py clean_environment.py /REST_API/
RUN pip install flask pip install pymysql pip install requests
RUN chmod 644 rest_server.py
CMD ["python", "Backend_testing.py","clean_enviroment.py"]
