# Use an official Python runtime as a parent image
FROM python:3.10-slim as builder

# Set the working directory in the container
WORKDIR /app

# Install FastAPI and Uvicorn
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Copy the application code to the build stage
COPY . .

# Stage 2: Run
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /root/.local /root/.local
COPY . .

# Ensure the Python path includes installed dependencies
ENV PATH=/root/.local/bin:$PATH

# Expose port 8000 to the outside world
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
