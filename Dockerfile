#  this is a sample docker file  for testing
FROM python:3.8 
RUN mkdir /app 
WORKDIR /app 
ADD . /app/ 
# Install git
RUN apt-get update && \
    apt-get install -y git
RUN pip install -r requirements.txt 
RUN git clone https://huggingface.co/TsinghuaAI/CPM-Generate
CMD ["python", "app.py"]
EXPOSE 8000
