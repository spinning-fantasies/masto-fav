import os
import json
from mastodon import Mastodon
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables

# Create an instance of the Mastodon class
mastodon = Mastodon(
    access_token = os.getenv('MASTODON_ACCESS_TOKEN'),
    api_base_url = os.getenv('MASTODON_INSTANCE_URL')
)

# Get the authenticated user's account
account = mastodon.account_verify_credentials()

# Get the authenticated user's statuses
statuses = mastodon.account_statuses(account['id'])

# Iterate through each status and retrieve favorites
for status in statuses:
    print(f"Status ID: {status['id']}")
    print(f"Status Content: {status['content']}")
    
    # Get favorites for the current status
    favorites = mastodon.status_favourited_by(status['id'])
    
    if favorites:
        print("Favorites:")
        for favorite in favorites:
            print(f"- {favorite['acct']}")
    else:
        print("No favorites for this status")
    
    print("\n")


