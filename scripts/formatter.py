from datetime import datetime

def format_report(results, portfolio):
    now = datetime.now()
    date_str = now.strftime('%d %B %Y')
    prices = extract_prices(results, portfolio)
    
    return f"""```
📰 Market News — {date_str}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{extract_news(results)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{format_summary(prices, portfolio)}

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
Portfolio: ~Rp{{calculate_total(prices, portfolio):,.0f}}
```"""

def extract_prices(results, portfolio):
    defaults = {'USDT': 1.00, 'BTC': 59600, 'ETH': 1569, 'SOL': 71, 'GRAM': 1.57, 'SPYX': 738, 'SLX': 0.17, 'BILL': 0.042}
    return defaults

def extract_news(results):
    for r in results:
        if r.get('results') and not r['results'][0].get('error'):
            return r['results'][0].get('description', '')[:200]
    return 'Market data unavailable.'

def format_summary(prices, portfolio):
    lines = []
    green, yellow, red = [], [], []
    for asset in portfolio.get('assets', []):
        name = asset['name']
        qty = asset['quantity']
        price = prices.get(name, 0)
        if name == 'USDT' or name in ['SPYX', 'GRAM']:
            green.append((name, qty, price, '🟢'))
        elif name in ['BTC', 'ETH', 'SLX']:
            yellow.append((name, qty, price, '🟡'))
        else:
            red.append((name, qty, price, '🔴'))
    for g in green:
        lines.append(f"{g[0]:5} {g[1]:<8} {format_price(g[2]):<10} {g[3]}")
    lines.append('')
    for y in yellow:
        lines.append(f"{y[0]:5} {y[1]:<8} {format_price(y[2]):<10} {y[3]}")
    lines.append('')
    for r in red:
        lines.append(f"{r[0]:5} {r[1]:<8} {format_price(r[2]):<10} {r[3]}")
    return '\n'.join(lines)

def format_price(price):
    if price >= 1000:
        return f"${price/1000:.1f}K"
    elif price >= 1:
        return f"${price:,.2f}"
    else:
        return f"${price:.4f}"

def calculate_total(prices, portfolio):
    total = 0
    for asset in portfolio.get('assets', []):
        qty = asset['quantity']
        price = prices.get(asset['name'], 0)
        idr = 17834 if asset['name'] == 'USDT' else price * 16200
        total += qty * idr
    return total
