# Telegram Media Downloader

This is a Python script that allows you to download all media (photos, videos, documents, etc.) from a public Telegram channel or a specific forum within a channel. The script uses the `telethon` library to interact with the Telegram API.

## Features
-   **Channel-wide download:** Download all media from a Telegram channel, from the most recent to the oldest messages.
-   **Forum Topic Support:** If the channel is a forum, you can select a specific topic to download media from.
-   **Concurrency:** Uses `asyncio` to download multiple files simultaneously, improving performance.

# To install the required dependencies, run: 
pip install -r requirements.txt


# Telegram API:
    Go to my.telegram.org and log in with your phone number.
    Click on "API development tools" and create a new application.
    Note down your API_ID and API_HASH 

Create .env file:
    Add your API credentials to this file in the following format:
    API_ID=your_api_id 
    API_HASH=your_api_hash

