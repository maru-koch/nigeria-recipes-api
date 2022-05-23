# specify the base Image

FROM python:3.9-alphine3.13
LABEL maintainer="Nwokocha Maruche"
ENV PYTHONUNBUFFER 1

COPY .requirements.txt tmp/requirements.txt
COPY .app /app
WORKDIR /app
EXPOSE 8000

# install virtual enviroment
# upgrade pip
# install requirements.txt
# remove temporary file to keep our image lightweight
# it is best practice not to run docker image as the root user

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

# run the image using the current django user
USER django-user