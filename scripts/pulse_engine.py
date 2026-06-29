"""
Pulse Engine - Main Script
5 engines, 1 intelligence. Multi-engine crypto news aggregator.
"""

import os
import sys
import yaml
import json
import asyncio
from datetime import datetime
from dotenv import load_dotenv

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engines.brave import BraveEngine
from engines.exa import ExaEngine
from engines.tavily import TavilyEngine
from engines.parallel import ParallelEngine
from engines.firecrawl import FirecrawlEngine
from formatter import format_report
from telegram import send_to_telegram

# Load environment variables
load_dotenv()

# Load config
def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

async def run_engine(engine_name, engine_config, portfolio):
    """Run a single search engine and return results."""
    try:
        if engine_name == 'brave':
            engine = BraveEngine()
        elif engine_name == 'exa':
            engine = ExaEngine()
        elif engine_name == 'tavily':
            engine = TavilyEngine()
        elif engine_name == 'parallel':
            engine = ParallelEngine()
        elif engine_name == 'firecrawl':
            engine = FirecrawlEngine()
        else:
            return None
        
        query = engine_config.get('query', '')
        results = await engine.search(query)
        return {
            'engine': engine_name,
            'sector': engine_config.get('sector', ''),
            'query': query,
            'results': results
        }
    except Exception as e:
        print(f"[ERROR] {engine_name}: {str(e)}")
        return None

async def main():
    """Main entry point."""
    # Load configs
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    engines_config = load_config(os.path.join(base_dir, 'config', 'engines.yaml'))
    portfolio_config = load_config(os.path.join(base_dir, 'config', 'portfolio.yaml'))
    
    # Run all engines in parallel
    tasks = []
    for engine_name, engine_config in engines_config.get('engines', {}).items():
        task = run_engine(engine_name, engine_config, portfolio_config)
        tasks.append(task)
    
    results = await asyncio.gather(*tasks)
    
    # Filter out None results
    valid_results = [r for r in results if r is not None]
    
    # Format report
    report = format_report(valid_results, portfolio_config)
    
    # Print report
    print(report)
    
    # Send to Telegram if configured
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    telegram_topic_id = os.getenv('TELEGRAM_TOPIC_ID')
    
    if telegram_token and telegram_chat_id:
        send_to_telegram(
            token=telegram_token,
            chat_id=telegram_chat_id,
            message=report,
            topic_id=telegram_topic_id
        )
        print("\n[OK] Sent to Telegram")
    
    return report

if __name__ == '__main__':
    asyncio.run(main())
