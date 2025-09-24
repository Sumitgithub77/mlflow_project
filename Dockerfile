# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set working directory inside the container
WORKDIR /app

# Copy the entire contents of the current directory to /app in the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port streamlit runs on
EXPOSE 8501

# Command to run the Streamlit app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
