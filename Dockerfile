# Use a lightweight Python image

FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the script and data files into the container
COPY scripts/text_processor.py /app/
COPY data /home/data/


# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Set the script to execute on container start
CMD ["python", "text_processor.py"]
