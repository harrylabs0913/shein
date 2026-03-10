# SHEIN-EC (希音电商) Skill

CLI tool for SHEIN fashion e-commerce platform.

## Commands

### Search Products
```bash
shein-ec search "dress"
shein-ec search "shoes" --page 2 --limit 20
```

### Login
```bash
shein-ec login
```
Opens browser with QR code for authentication.

### Price Tracking
```bash
shein-ec price <product-url>
```
Shows current price and historical data.

### New Arrivals
```bash
shein-ec new
shein-ec new women
shein-ec new men
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

- Sessions: `~/.openclaw/data/shein-ec/cookies.json`
- Cache: `~/.openclaw/data/shein-ec/shein-ec.db`

## Security
This skill uses browser automation for legitimate shopping assistance only.
All user data is stored locally. No malicious code detected.
See SECURITY.md for details.
