FROM python:3.9.15-slim-buster

# Set a directory for the app
WORKDIR /home

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy all the files to the container
COPY . .

# Define the port number the container should expose
EXPOSE 8501

# Run the command
CMD ["streamlit", "run", "wine-streamlit.py"]
