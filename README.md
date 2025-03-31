# YouTube Channel Scraper

A Flask application for scraping YouTube channels based on various criteria.

## Deployment Instructions for cPanel

1. **Upload Files**
   - Upload all files to your cPanel hosting directory
   - Make sure to maintain the directory structure:
     ```
     your_domain/
     ├── youtube_scraper/
     │   ├── app.py
     │   ├── static/
     │   └── templates/
     ├── requirements.txt
     ├── passenger_wsgi.py
     └── .htaccess
     ```

2. **Set Up Python Environment**
   - Log in to cPanel
   - Go to "Setup Python App"
   - Create a new Python application
   - Select Python 3.8 or higher
   - Set the application root to your domain directory
   - Set the application URL to your domain
   - Set the application startup file to `passenger_wsgi.py`

3. **Install Dependencies**
   - In cPanel, go to "Terminal"
   - Navigate to your application directory
   - Create and activate a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Install requirements:
     ```bash
     pip install -r requirements.txt
     ```

4. **Configure passenger_wsgi.py**
   - Edit `passenger_wsgi.py`
   - Replace `YOUR_CPANEL_USERNAME` with your cPanel username
   - Update the Python path to match your virtual environment path

5. **Set Up Application**
   - In cPanel, go to "Setup Python App"
   - Click on your application
   - Click "Restart" to apply changes

6. **File Permissions**
   - Set proper permissions for your files:
     ```bash
     chmod 755 passenger_wsgi.py
     chmod 755 youtube_scraper/app.py
     chmod -R 755 youtube_scraper/static
     chmod -R 755 youtube_scraper/templates
     chmod 644 .htaccess
     ```

7. **Environment Variables**
   - In cPanel, go to "Setup Python App"
   - Add the following environment variables:
     ```
     FLASK_ENV=production
     FLASK_APP=youtube_scraper.app
     ```

8. **Troubleshooting**
   - Check error logs in cPanel's "Error Log"
   - Make sure all file paths are correct
   - Verify Python version compatibility
   - Ensure all dependencies are installed correctly

## Features
- Search YouTube channels by various criteria
- Export results to Excel
- Proxy rotation support
- Progress tracking
- Error handling and retries

## Requirements
- Python 3.8 or higher
- Flask
- google-api-python-client
- pandas
- requests
- httplib2
- gunicorn

## Support
For support or questions, please contact your hosting provider or refer to the error logs in cPanel. 