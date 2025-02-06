# Step 1: Use an official Python runtime as the base image
FROM python:3.13.1

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy requirements.txt first
COPY requirements.txt /app/

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the project files
COPY . /app

# Step 6: Expose port (default Flask port)
EXPOSE 5000

# Step 7: Run the app using Gunicorn
CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:5000", "app:app"]
