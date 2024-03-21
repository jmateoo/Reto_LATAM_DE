This project is a Flask application that processes a JSON file containing tweets. The application has six main functions: q1_time, q1_memory, q2_time, q2_memory, q3_time, and q3_memory. Each function processes the file in a different way, and their performance is measured in terms of time and memory usage.

To run this application, you will need Python 3.9 and Flask installed on your machine. You can start the application by running

```bash
python3 main.py




To run this application in Docker

```bash
docker build -t my-app .

```bash
docker run -p 80:80 my-flask-app

