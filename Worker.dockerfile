# Base Image
FROM python:3

ADD ./requirements.txt  /requirements.txt

# install required packages via PIP
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r /requirements.txt

# Copy project files
ADD  src/ /opt/worker/

# Set a work dir
WORKDIR /opt/worker/
ENV PYTHONUNBUFFERED=1

# Tell the docker which cmd to run when using this image
ENTRYPOINT ["celery", "-A", "tasks", "worker"]