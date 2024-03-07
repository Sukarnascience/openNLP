# Use Python 3.7 as the base image
FROM python:3.7

# Set the working directory
WORKDIR /app

# Copy the setup.sh file into the container
COPY setup_linux. /app/

# Run the setup.sh file
RUN chmod +x setup_linux.sh && ./setup_linux.sh

# Copy the rest of your application files into the container
COPY . /app

# Set the entry point for the container (replace 'your_script.py' with your actual Python script)
CMD ["python", "offlineNLP.py"]
