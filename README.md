# Automated Web Scraper with Instant Data Scraper Extension

This project automates batch processing of URLs using the Instant Data Scraper Chrome extension. It programmatically controls the extension to extract tabular data from multiple web pages, eliminating the need for manual extension activation and data downloading for each URL.

## The script will:

- Read URLs from queue.txt
- Process each URL automatically
- Move processed URLs to crawled.txt
- Save extracted data as CSV files

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

2. Add your target URLs to queue.txt, one URL per line

3. Run the scraper:

```bash
python main.py
```


## Features
- Batch URL processing from queue.txt
- Automated extension workflow for each URL:
  - Extension activation
  - Data extraction
  - CSV download
  - Extension closure
- Tracking of processed URLs in crawled.txt
- CAPTCHA detection
- Logging system

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
