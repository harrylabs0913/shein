# SHEIN-EC (希音电商) Skill

CLI tool for SHEIN fashion e-commerce platform.

## Commands

### Search Products
```bash
shein-shopping search "dress"
shein-shopping search "shoes" --page 2 --limit 20
```

### Login
```bash
shein-shopping login
```
Opens browser with QR code for authentication.

### Price Tracking
```bash
shein-shopping price <product-url>
```
Shows current price and historical data.

### New Arrivals
```bash
shein-shopping new
shein-shopping new women
shein-shopping new men
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

- Sessions: `~/.openclaw/data/shein-shopping/cookies.json`
- Cache: `~/.openclaw/data/shein-shopping/shein-shopping.db`

## Security
This skill uses browser automation for legitimate shopping assistance only.
All user data is stored locally. No malicious code detected.
See SECURITY.md for details.
