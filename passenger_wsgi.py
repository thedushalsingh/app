import sys
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the application directory to the Python path
sys.path.insert(0, current_dir)

# Import the Flask application
from youtube_scraper.app import app as application 