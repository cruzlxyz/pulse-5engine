import os
import aiohttp

class TavilyEngine:
    def __init__(self):
        self.api_key = os.getenv('TAVILY_API_KEY')
        self.base_url = 'https://api.tavily.com/search'
    
    async def search(self, query):
        if not self.api_key:
            return [{'error': 'TAVILY_API_KEY not set'}]
        data = {'api_key': self.api_key, 'query': query, 'max_results': 5, 'search_depth': 'basic'}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.base_url, json=data) as r:
                    if r.status == 200:
                        result = await r.json()
                        return [{'title': i.get('title',''), 'url': i.get('url',''), 'description': i.get('content','')[:200]} for i in result.get('results',[])]
                    return [{'error': f'API error: {r.status}'}]
        except Exception as e:
            return [{'error': str(e)}]
