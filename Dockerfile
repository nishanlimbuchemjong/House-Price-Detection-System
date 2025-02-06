# Step 1: Used an official Python runtime as the base image
FROM python:3.13.1

# Step 2: Copy the current directory contents into the container
COPY  requirements.txt /app/

# Step 3: Set the working directory in the container
WORKDIR /app.1

# Step 4: Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the project files
COPY . /app

# Step 5: Expose port (Flask default port)
EXPOSE $PORT

# Step 6: Run the app using Gunicorn (you can also use Flask's built-in server, but Gunicorn is preferred for production)
CMD Gunicorn ==workers=4 --bind 0.0.0.0:$PORT app:app
