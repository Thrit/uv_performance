# Use the official Python image as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements.txt file into the container at /app
COPY requirements.txt .

# Create a virtual environment
RUN python -m venv venv

# Activate the virtual environment and install uv library
SHELL ["/bin/bash", "-c"]
RUN source venv/bin/activate \
    && pip install uv

# Install dependencies from requirements.txt using uv-pip
RUN source venv/bin/activate \
    && uv pip install -r requirements.txt

# Copy the rest of your application files into the container
COPY . .

# Command to run your application
CMD ["python", "performance.py"]
