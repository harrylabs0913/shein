# SHEIN (希音) Skill

CLI tool for SHEIN fashion e-commerce platform.

## Commands

### Search Products
```bash
shein search "dress"
shein search "shoes" --page 2 --limit 20
```

### Login
```bash
shein login
```
Opens browser with QR code for authentication.

### Price Tracking
```bash
shein price <product-url>
```
Shows current price and historical price data.

### New Arrivals
```bash
shein new
shein new women
shein new men
```
Query new arrivals by category.

## Features

- Product search with caching
- QR code login
- Price history tracking
- New arrivals query
- Anti-detection browser automation

## Dependencies

- `playwright>=1.40.0` - Browser automation

## Data Storage

- Sessions: `~/.openclaw/data/shein/cookies.json`
- Cache: `~/.openclaw/data/shein/shein.db`

## Security
This skill uses browser automation for legitimate shopping assistance only.
All user data is stored locally. No malicious code detected.
See SECURITY.md for details.
