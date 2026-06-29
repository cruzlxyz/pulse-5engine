# 💓 Pulse 5Engine

> 5 engines, 1 intelligence. Multi-engine crypto news aggregator built for [Hermes Agent](https://hermes-agent.nousresearch.com).

## 🔍 Overview

Pulse 5Engine searches across 5 different search engines simultaneously, each covering a specific sector, and delivers a formatted portfolio report directly to your Telegram forum via Hermes Agent cron jobs.

| # | Engine | Sector | Focus |
|---|--------|--------|-------|
| 1 | 🔍 Brave | 💰 Prices | Real-time portfolio prices |
| 2 | 🧠 Exa | 🏛️ Regulation | SEC, tokenized securities, DeFi |
| 3 | 🤖 Tavily | 🤖 AI + Airdrop + RWA | AI agents, pre-TGE, tokenized stocks |
| 4 | ⚡ Parallel | 🛡️ Security | DeFi exploits, vulnerabilities |
| 5 | 🕷️ Firecrawl | 🌍 Macro | Fed rate, ETF flows, geopolitics |

## 🚀 Quick Start

```bash
git clone https://github.com/cruzlxyz/pulse-5engine.git
cd pulse-5engine
pip install -r requirements.txt
cp .env.example .env
```

## 🔑 Get API Keys (All Free Tier)

| Engine | Get API Key | Free |
|--------|-------------|------|
| 🔍 Brave | https://api.search.brave.com/register | 2,000/month |
| 🧠 Exa | https://exa.ai | 1,000/month |
| 🤖 Tavily | https://app.tavily.com | 1,000/month |
| ⚡ Parallel | https://parallel.ai | Free tier |
| 🕷️ Firecrawl | https://firecrawl.dev | 1,000/month |

Edit `.env`:
```env
BRAVE_API_KEY=***## 🤖 Hermes Agent Integration

### Method 1: Cron Job (Recommended)

Pulse 5Engine works as a Hermes Agent cron job. This is the easiest way to get daily automated reports.

#### Step 1: Setup Hermes Agent
Make sure Hermes Agent is installed and running with Telegram integration.

#### Step 2: Add API Keys to Hermes `.env`
Add your API keys to `~/.hermes/.env` or `%LOCALAPPDATA%/hermes/.env`:
```env
BRAVE_API_KEY=***
EXA_API_KEY=***
TAVILY_API_KEY=***
PARALLEL_API_KEY=***
FIRECRAWL_API_KEY=***
```

#### Step 3: Create Cron Job
Run this in Hermes Agent chat:
```
Create a cron job called "daily-portfolio-news" that runs every day at 7 AM.
The job should:
1. Search using all 5 engines (Brave, Exa, Tavily, Parallel, Firecrawl)
2. Format results as a code block with sections: Market News, Summary, Advisor, Reminder
3. Deliver to my Telegram forum topic
```

Or use the Hermes CLI:
```bash
hermes cron create \
  --name "daily-portfolio-news" \
  --schedule "0 7 * * *" \
  --deliver "telegram:YOUR_CHAT_ID:YOUR_TOPIC_ID" \
  --prompt "Search using all 5 engines and format as code block..."
```

#### Step 4: Configure Your Portfolio
Edit `config/portfolio.yaml` with your assets:
```yaml
assets:
  - name: BTC
    quantity: 0.01
  - name: ETH
    quantity: 0.4
  # ... add your assets
```

#### Step 5: Test
```bash
hermes cron run daily-portfolio-news
```

### Method 2: Standalone Script

Run Pulse 5Engine directly without Hermes Agent:

```bash
# Set environment variables
export BRAVE_API_KEY=***
export EXA_API_KEY=***
export TAVILY_API_KEY=***
export PARALLEL_API_KEY=***
export FIRECRAWL_API_KEY=***

# Run
python scripts/pulse_engine.py
```

### Method 3: GitHub Actions

Automate with GitHub Actions (runs daily at 7 AM UTC):

1. Go to your repo → Settings → Secrets and variables → Actions
2. Add all API keys as repository secrets
3. The workflow in `.github/workflows/daily-news.yml` will run automatically

## ⚙️ Configuration

### Engine Queries (`config/engines.yaml`)
```yaml
engines:
  brave:
    query: "BTC ETH SOL GRAM SPYX SLX BILL price today USD"
  exa:
    query: "SEC crypto regulation framework tokenized securities DeFi 2026"
  tavily:
    query: "AI agents airdrop pre-TGE RWA tokenized stocks news 2026"
  parallel:
    query: "crypto hack exploit DeFi vulnerability security alert 2026"
  firecrawl:
    query: "Federal Reserve interest rate Bitcoin ETF geopolitical crypto 2026"
```

### Portfolio (`config/portfolio.yaml`)
```yaml
assets:
  - name: USDT
    quantity: 2100
  - name: BTC
    quantity: 0.01
  - name: ETH
    quantity: 0.4
  - name: SOL
    quantity: 2
  - name: GRAM
    quantity: 3
  - name: SPYX
    quantity: 0.11
  - name: SLX
    quantity: 931.65
  - name: BILL
    quantity: 5618
```

## 📋 Output Format

```
📰 Market News — 29 Juni 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Market news in Indonesian]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

USDT  2,100   $1.00    🟢
SPYX  0.11    $738     🟢
GRAM  3       $1.57    🟢

BTC   0.01    $59.6K   🟡
ETH   0.4     $1,569   🟡
SLX   931.65  $0.17    🟡

SOL   2       $71      🔴
BILL  5,618   $0.042   🔴

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 Advisor
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Jual   : BILL — low volume, high risk
Hold   : BTC, ETH — accumulation phase
Beli   : SPYX — RWA narrative hot
Hindari: SOL — bearish pattern

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏰ Reminder
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- 5 Jul — SLX unlock
- 31 Oct — BILL unlock

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Portfolio: ~Rp69,800,000
```

## 📁 Structure

```
pulse-5engine/
├── .github/workflows/
│   └── daily-news.yml
├── scripts/
│   ├── pulse_engine.py
│   ├── engines/
│   │   ├── __init__.py
│   │   ├── brave.py
│   │   ├── exa.py
│   │   ├── tavily.py
│   │   ├── parallel.py
│   │   └── firecrawl.py
│   ├── formatter.py
│   └── telegram.py
├── config/
│   ├── engines.yaml
│   └── portfolio.yaml
├── .env.example
├── requirements.txt
├── LICENSE
└── README.md
```

## 🔒 Security

- Never commit `.env` file
- API keys are stored locally only
- Each engine has its own free tier
- Total daily usage: 5 queries (well within free limits)

## 📊 Free Tier Summary

| Engine | Free Quota | Daily Usage | Status |
|--------|-----------|-------------|--------|
| Brave | 2,000/month | 30/month | ✅ Safe |
| Exa | 1,000/month | 30/month | ✅ Safe |
| Tavily | 1,000/month | 30/month | ✅ Safe |
| Parallel | Free tier | 30/month | ✅ Safe |
| Firecrawl | 1,000/month | 30/month | ✅ Safe |

## 🤝 Contributing

PRs welcome!

## 📄 License

MIT

---

Built with 💓 by [cruzlxyz](https://github.com/cruzlxyz)
Powered by [Hermes Agent](https://hermes-agent.nousresearch.com)
