# Base Image
FROM python:3

ADD ./requirements.txt  /requirements.txt

# install required packages via PIP
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r /requirements.txt

# Copy project files
ADD  src/ /opt/api/

# Set a work dir
WORKDIR /opt/api/
ENV PYTHONUNBUFFERED=1

# Tell the docker which cmd to run when using this image
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0"]