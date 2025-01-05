# Automated Web Scraper with Instant Data Scraper Extension

This project automates web scraping using Selenium WebDriver and the Instant Data Scraper Chrome extension. It's designed to automatically extract tabular data from web pages by programmatically controlling the extension.

## Prerequisites

- Python 3.7+
- Chrome browser
- [Instant Data Scraper Extension](https://chromewebstore.google.com/detail/instant-data-scraper/ofaokhiedipichpaobibbnahnkdoiiah)
- ChromeDriver (matching your Chrome version)

## Required Python Packages

```bash
pip install selenium
pip install pyautogui
pip install pandas
```

## Project Structure

```
├── src/
│   ├── utils.py                 # Core web scraping functionality
│   ├── instant_data_scraper.py  # Extension automation logic
│   └── main.py                  # Entry point and project setup
├── assets/
│   ├── chromedriver-win64/      # Chrome WebDriver files
│   └── instant_data_scraper_extension/  # Extension files
└── scraper_log.log        # Logging output
```

## Important Note

The current implementation uses hardcoded screen coordinates for automating the extension interface. These coordinates are set for a specific screen resolution and will need to be adjusted for different displays:

- Chrome extension button: (1762, 94)
- Extension activate button: (1460, 302)
- Download CSV button: (1003, 153)
- Extension close button: (1883, 14)

## Usage

1. Update the paths in `main.py`:

```python
chromedriver_path = 'path/to/your/chromedriver.exe'
instant_data_scraper_path = 'path/to/extension.crx'
url = "your_target_url"
```

2. Run the scraper:

```bash
python main.py
```

## Features

- Automated Chrome extension control
- CAPTCHA detection
- Logging system
- File management for crawled URLs
- Automatic CSV data extraction

## Limitations

1. Screen Resolution Dependency
   - The automation relies on specific screen coordinates
   - Will only work on screens matching the coded resolution

2. Single Page Scraping
   - Currently handles only single pages
   - Pagination support is implemented but commented out

3. Error Handling
   - Basic error handling for CAPTCHA detection
   - Limited handling for extension failures

## Future Improvements

1. Dynamic coordinate calculation for extension interaction
2. Implement robust pagination handling
3. Add retry mechanisms for failed scraping attempts
4. Enhance error handling and recovery
5. Add support for multiple URL processing
6. Implement configuration file for easy customization

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational purposes only. Make sure to comply with the target website's terms of service and robots.txt file before scraping. Always include appropriate delays between requests to avoid overwhelming servers.
