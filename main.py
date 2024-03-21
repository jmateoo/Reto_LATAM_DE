from flask import Flask, jsonify, request, current_app
from datetime import datetime
import os
from src.q1_time import q1_time
from src.q1_memory import q1_memory
from src.q2_time import q2_time
from src.q2_memory import q2_memory
from src.q3_time import q3_time
from src.q3_memory import q3_memory
import logging
from threading import Thread

app = Flask(__name__)
print("Started.")

@app.route('/run', methods=['GET']) 
def process_files():
    with app.app_context():
        # Set up logging
        logging.basicConfig(filename='process_files.log', level=logging.INFO)

        try:
            logging.info("Starting functions...")
            file_path = "/Users/josemateoaristizabaldiaz/downloads/farmers-protest-tweets-2021-2-4.json"
            q1_time(file_path)
            q1_memory(file_path)
            q2_time(file_path)
            q2_memory(file_path)
            q3_time(file_path)
            q3_memory(file_path)
            return jsonify({'message': 'Processing finished'}), 200

        except Exception as e:
            logging.error(f"Error: {str(e)}")
            return jsonify({'message': f'Error: {str(e)}'}), 500

if __name__ == "__main__":
    print("Starting API on port 80.")
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 80)))