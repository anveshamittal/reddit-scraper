# reddit-scraper

This project scrapes a Reddit user's public comments, chunks and embeds them, and uses a local LLM (via HuggingFace or Azure OpenAI) to infer their persona.

## 📦 Setup

### 1. Clone the repository
git clone https://github.com/anveshamittal/reddit-scraper.git

### 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # for linux/mac
.venv\Scripts\activate           # for windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. 4. Setup your .env file
Create a .env file in the root directory with the following:
# Reddit API credentials (get from https://www.reddit.com/prefs/apps)
CLIENT_ID=your_reddit_client_id
CLIENT_SECRET=your_reddit_secret
USER_AGENT=your_app_name

# Azure OpenAI (if using Azure-based embedding and LLM)
AZURE_OPENAI_ENDPOINT=https://your-instance-name.openai.azure.com
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-mini-custom

### 5.Edit extract_data.py in src->db to target a Reddit username:
username = enter your username there

### 6. Run python main.py
