# 💓 Pulse Engine

> 5 engines, 1 intelligence. Multi-engine crypto news aggregator powered by Brave, Exa, Tavily, Parallel, and Firecrawl.

## 🔍 Overview

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
cd pulse-engine
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
BRAVE_API_KEY=***
EXA_API_KEY=***
TAVILY_API_KEY=***
PARALLEL_API_KEY=***
FIRECRAWL_API_KEY=***
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
pulse-engine/
├── .github/workflows/
├── scripts/
│   ├── pulse_engine.py
│   ├── engines/
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

## 📄 License

MIT

---

Built with 💓 by [cruzlxyz](https://github.com/cruzlxyz)
