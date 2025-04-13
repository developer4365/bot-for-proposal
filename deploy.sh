#!/bin/bash

# Install dependencies
if ! pip install -r requirements.txt; then
    echo "Failed to install dependencies. Please check your requirements.txt file."
    exit 1
fi

# Set up environment variables
if [ ! -f ".env" ]; then
    echo "Creating .env file from example"
    cp .env.example .env
    echo "Please edit the .env file with your Telegram bot token and ID"
    exit 1
fi

# Start the bot using PM2 for process management
if ! command -v pm2 &> /dev/null
then
    echo "PM2 not found, installing..."
    if ! npm install -g pm2; then
        echo "Failed to install PM2. Please ensure Node.js and npm are installed."
        exit 1
    fi
fi

if ! pm2 start bot.py --name proposal-bot --interpreter python3; then
    echo "Failed to start the bot with PM2."
    exit 1
fi

pm2 save
pm2 startup

echo "Bot deployed successfully!"
echo "To view logs: pm2 logs proposal-bot"
echo "To stop: pm2 stop proposal-bot"
