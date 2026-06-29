import os
import aiohttp

class FirecrawlEngine:
    def __init__(self):
        self.api_key = os.getenv('FIRECRAWL_API_KEY')
        self.base_url = 'https://api.firecrawl.dev/v1/search'
    
    async def search(self, query):
        if not self.api_key:
            return [{'error': 'FIRECRAWL_API_KEY not set'}]
        headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {self.api_key}'}
        data = {'query': query, 'limit': 5}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.base_url, headers=headers, json=data) as r:
                    if r.status == 200:
                        result = await r.json()
                        return [{'title': i.get('metadata',{}).get('title',''), 'url': i.get('url',''), 'description': i.get('markdown','')[:200] if i.get('markdown') else ''} for i in result.get('data',[])]
                    return [{'error': f'API error: {r.status}'}]
        except Exception as e:
            return [{'error': str(e)}]
