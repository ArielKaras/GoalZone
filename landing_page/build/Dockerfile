FROM python:3.11.1-slim-bullseye
WORKDIR /app/landing_page
ENV APP_PATH=/app/landing_page
ENV PYTHONPATH=/app/landing_page
COPY  .. .
RUN apt-get update
RUN apt remove -fy libaom0:amd64
RUN  echo "PWD is: $PWD" && ls -la
RUN pip install -r requirements.txt
ENV PATH="${PATH}:${FLASK_APP}"
RUN export FLASK_APP=landing_page/__init__.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]