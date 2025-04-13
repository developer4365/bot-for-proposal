import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch required environment variables
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_TELEGRAM_ID')

# Ensure required variables are not missing
if not TOKEN or not ADMIN_ID:
    raise ValueError("Missing required environment variables: TELEGRAM_BOT_TOKEN or ADMIN_TELEGRAM_ID")
