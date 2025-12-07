# Email Breach Checker

A Python script that checks email addresses against the LeakCheck.io public API to verify if they have been involved in data breaches.

## Features

- Check single email addresses for breach involvement
- Batch check multiple email addresses from a file
- Automatic email validation using regex
- Color-coded terminal output (green for safe, red for compromised)
- Export results to a timestamped output file
- Rate limiting to respect API constraints

## Requirements

- Python 3.x
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- Required packages:
  ```bash
  uv pip install requests termcolor
  ```
  
  Or with pip:
  ```bash
  pip install requests termcolor
  ```

## Usage

### Check a Single Email

```bash
./email-breach-checker.py -email user@example.com
```

### Check Multiple Emails from a File

```bash
./email-breach-checker.py -inputfile emails.txt
```

### Specify Custom Output File

```bash
./email-breach-checker.py -inputfile emails.txt -outputfile results.txt
```

## Arguments

- `-email`: Single email address to check for breaches
- `-inputfile`: Path to a text file containing email addresses (one per line)
- `-outputfile`: Path for the output file (default: `email-breach-check-results-YYYY-MM-DD_HH-MM-SS.txt`)

## Input File Format

The input file should contain one email address per line:

```
user1@example.com
user2@example.com
user3@example.com
```

Invalid email addresses will be automatically skipped.

## Output

- **Terminal**: Color-coded results showing which services each email has been compromised on
  - Green: No breaches found
  - Red: Breaches detected with list of affected services
- **File**: Detailed results saved to the specified output file (batch mode only)

## Notes

- The script includes a 3-second delay between API requests to avoid rate limiting
- Uses the LeakCheck.io public API (no authentication required)
- Email validation is performed using regex pattern matching

## Acknowledgments

This tool uses the [LeakCheck.io](https://leakcheck.io/) public API. Special thanks to LeakCheck for providing free access to their breach database, making it possible to check email security easily and efficiently.

## Example Output

```
user@example.com : ['LinkedIn', 'Adobe', 'Dropbox']
safe@example.com : No breaches found
```

## Disclaimer

This tool is for educational and security awareness purposes. Always ensure you have permission to check email addresses and handle the results responsibly.
