# Enhanced Chatbot with Social Media Integration for Portfolio (Optimized for Deployment with Analytics)

# Install required libraries
# pip install flask transformers facebook-sdk linkedin-api python-dotenv torch

from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer
from facebook import GraphAPI
from linkedin_api import Linkedin
from dotenv import load_dotenv
import os
import torch
import logging
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__, template_folder='templates')

# Configure logging
logging.basicConfig(
    filename='app_logs.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# Load lightweight GPT model for chatbot responses
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Load API credentials from environment variables
FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")
LINKEDIN_USERNAME = os.getenv("LINKEDIN_USERNAME")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")

# Initialize social media APIs
facebook_graph = GraphAPI(access_token=FACEBOOK_ACCESS_TOKEN)
linkedin = Linkedin(LINKEDIN_USERNAME, LINKEDIN_PASSWORD)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400

    try:
        input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors="pt")
        output = model.generate(input_ids, max_length=100, pad_token_id=tokenizer.eos_token_id)
        reply = tokenizer.decode(output[0], skip_special_tokens=True)
        logging.info(f"Chat Request: '{user_message}' | Response: '{reply}'")
        return jsonify({"response": reply})
    except Exception as e:
        logging.error(f"Chat Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/post-to-facebook", methods=["POST"])
def post_to_facebook():
    post_content = request.json.get("content")
    if not post_content:
        return jsonify({"error": "Content cannot be empty"}), 400

    try:
        response = facebook_graph.put_object(parent_object='me', connection_name='feed', message=post_content)
        logging.info(f"Posted to Facebook: {post_content}")
        return jsonify({"success": True, "post_id": response['id']})
    except Exception as e:
        logging.error(f"Facebook Post Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/post-to-linkedin", methods=["POST"])
def post_to_linkedin():
    post_content = request.json.get("content")
    if not post_content:
        return jsonify({"error": "Content cannot be empty"}), 400

    try:
        linkedin.submit_share(post_content)
        logging.info(f"Posted to LinkedIn: {post_content}")
        return jsonify({"success": True})
    except Exception as e:
        logging.error(f"LinkedIn Post Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return render_template("index.html")

# Run the Flask server
if __name__ == "__main__":
    app.run(debug=True, port=5000)
