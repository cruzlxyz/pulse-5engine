import os
import aiohttp

class ExaEngine:
    def __init__(self):
        self.api_key = os.getenv('EXA_API_KEY')
        self.base_url = 'https://api.exa.ai/search'
    
    async def search(self, query):
        if not self.api_key:
            return [{'error': 'EXA_API_KEY not set'}]
        headers = {'Content-Type': 'application/json', 'x-api-key': self.api_key}
        data = {'query': query, 'numResults': 5, 'type': 'auto'}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.base_url, headers=headers, json=data) as r:
                    if r.status == 200:
                        result = await r.json()
                        return [{'title': i.get('title',''), 'url': i.get('url',''), 'description': i.get('text','')[:200]} for i in result.get('results',[])]
                    return [{'error': f'API error: {r.status}'}]
        except Exception as e:
            return [{'error': str(e)}]
