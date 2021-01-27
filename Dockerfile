FROM fnndsc/ubuntu-python3
COPY ./ /infracloud
WORKDIR /infracloud
RUN pip3 install -r requirements.txt
EXPOSE 8000
ENTRYPOINT [ "uvicorn",  "main:app" ]
