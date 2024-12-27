import requests
import re
import json
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import os

# Configuration (replace these with your actual values)
YOUTUBE_CHANNELS = os.environ.get("YOUTUBE_CHANNELS", "UCt8llfhkf9LRzjTEnbG2qnQ,UCb2O5Uo4a26CdTE7_2QA-jA,UCHLqIOMPk20w-6cFgkA90jw,UC0V3IJCnr6ZNjB9t_GLhFFA,UCWVqdPTigfQ-cSNwG7O9MeA,UC2P5Fd5g41Gtdqf0Uzh8Qaw,UCxHoBXkY88Tb8z1Ssj6CWsQ,UCN6sm8iHiPd0cnoUardDAnw,UCtqvtAVmad5zywaziN6CbfA,UCUvXoiDEKI8VZJrr58g4VAw,UC8NcXMG3A3f2aFQyGTpSNww,UCmCCTsDl-eCKw91shC7ZmMw,UCATUkaOHwO9EP_W87zCiPbA").split(",")
PLAYLIST_ID = os.environ.get("PLhDI33oYisToytKQ-gNFqG9Mx4XmOCmNA") # Your YouTube playlist ID
API_KEY = os.environ.get("AIzaSyCCEdOKSh_Axvs5qF87xtjWVvAmCGysc6U") # Your YouTube Data API v3 key
CHECK_INTERVAL_SECONDS = int(os.environ.get("CHECK_INTERVAL_SECONDS", 600)) # How often to check for new streams (default: 10 minutes)
MAX_AGE_SECONDS = int(os.environ.get("MAX_AGE_SECONDS", 3600)) # How long a stream can be considered "live" after it ends (default: 1 hour)

# ... (rest of the code remains the same)
