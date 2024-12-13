FROM python:3.10-slim

WORKDIR /codingTools

# Copying the requirements file before installing dependencies
COPY requirements.txt /codingTools/

# Installing just what we need, keeping the image small and efficient
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Installing ffmpeg
    python3-venv ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Creating a virtual environment
RUN python -m venv /app/venv

# Activate the virtual environment and install dependencies
RUN /app/venv/bin/pip install --no-cache-dir --upgrade pip && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the files
COPY . /codingTools

# Set the virtual environment as the default Python environment
ENV PATH="/app/venv/bin:$PATH"

# Running the menu script
CMD ["python", "menu.py"]