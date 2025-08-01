# 🧠 Chatbot with Social Media Integration (Flask + distilgpt2)

This Flask app integrates a conversational AI chatbot powered by `distilgpt2` with direct posting capabilities to Facebook and LinkedIn.

## 🚀 Features
- **Conversational AI** via Hugging Face's `distilgpt2`
- **Post to Facebook** using Graph API
- **Post to LinkedIn** using `linkedin-api`
- **Front-end interface** for chatbot interaction
- **Secure credentials** using `.env` and `python-dotenv`

## 🛠 Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/chatbot-social
cd chatbot-social
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure `.env`
Rename `.env.example` to `.env` and replace with your actual credentials:
```env
FACEBOOK_ACCESS_TOKEN=your_facebook_token
LINKEDIN_USERNAME=your_email
LINKEDIN_PASSWORD=your_password
```

### 4. Run the app
```bash
python app.py
```

## 🔧 Endpoints

| Endpoint            | Method | Description                        |
|---------------------|--------|------------------------------------|
| `/`                 | GET    | Frontend chat interface            |
| `/chat`             | POST   | Send a message to the chatbot      |
| `/post-to-facebook` | POST   | Post a message to Facebook         |
| `/post-to-linkedin` | POST   | Post a message to LinkedIn         |

## 📦 Example Request

```json
POST /chat
{
  "message": "Hello!"
}
```

## 📸 Front-End Preview
A clean HTML5 chat interface is provided in `/templates/index.html`.

---

© 2025 Brandon B. Gibbs | [@LilBDataGuy](https://github.com/lilbdataguy)