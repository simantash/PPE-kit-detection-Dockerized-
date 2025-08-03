# Use Python as base image
FROM python:3.10-slim


# Set working directory inside the container
WORKDIR /app

# Copy everything into the container
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# For OpenCV to work (especially for webcam)
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# Set default command to run your app
CMD ["python", "ppe_detection.py"]

