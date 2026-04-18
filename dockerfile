FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    python3-pyaudio \
    espeak \
    && apt-get clean

# Working directory
WORKDIR /app

# Copy project
COPY . /app

# Install Python libraries
RUN pip install --no-cache-dir eel

# Port
EXPOSE 8000

# Run your main file (IMPORTANT)
CMD ["python", "main.py"]