FROM python:3.11.1-slim-bullseye
WORKDIR /app
ENV FLASK_APP=landing_page/__init__.py
ENV PYTHONPATH=/app/landing_page
ENV PATH="${PATH}:${FLASK_APP}"
COPY  .. .
RUN apt-get update
RUN apt remove -fy libaom0:amd64
RUN pip install -r requirements.txt
RUN export FLASK_APP=${FLASK_APP}
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]