import os
import aiohttp

class ParallelEngine:
    def __init__(self):
        self.api_key = os.getenv('PARALLEL_API_KEY')
        self.base_url = 'https://api.parallel.ai/v1/search'
    
    async def search(self, query):
        if not self.api_key:
            return [{'error': 'PARALLEL_API_KEY not set'}]
        headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {self.api_key}'}
        data = {'query': query, 'max_results': 5}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.base_url, headers=headers, json=data) as r:
                    if r.status == 200:
                        result = await r.json()
                        return [{'title': i.get('title',''), 'url': i.get('url',''), 'description': i.get('snippet','')[:200]} for i in result.get('results',[])]
                    return [{'error': f'API error: {r.status}'}]
        except Exception as e:
            return [{'error': str(e)}]
