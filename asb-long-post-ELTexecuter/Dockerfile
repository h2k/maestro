FROM python:3.12

COPY . /
RUN ls -la /
RUN /usr/local/bin/python -m pip install --upgrade pip
# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

# Run the command on container startup
CMD [ "python", "main.py" ]