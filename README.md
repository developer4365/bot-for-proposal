# Romantic Proposal Telegram Bot

A Telegram bot that proposes to someone special with interactive buttons.

## Features
- 11 interactive buttons with custom messages
- Ability to send different files with each button
- Easy deployment on VPS

## Setup
1. Clone this repository by running:
   ```bash
   git clone https://github.com/your-username/romantic-proposal-bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd romantic-proposal-bot
   ```
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure your bot token in `.env`.

## Deployment
Use PM2 to keep the bot running:
```bash
pm2 start bot.py --name proposal-bot
```

## Updating Messages
To update the messages displayed by the buttons, use the `update_message.py` script:
```bash
python update_message.py
```

Follow the script's prompts to update a specific button's message or file.
