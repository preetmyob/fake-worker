FROM python:latest

# Set the working directory 
WORKDIR /app

#pip install requests
RUN pip install requests

# Copy the current directory contents into the container at /app
COPY . /app

# Run worker.py when the container launches 
CMD ["python", "worker.py"]