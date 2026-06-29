import os
import aiohttp

class BraveEngine:
    def __init__(self):
        self.api_key = os.getenv('BRAVE_API_KEY')
        self.base_url = 'https://api.search.brave.com/res/v1/web/search'
    
    async def search(self, query):
        if not self.api_key:
            return [{'error': 'BRAVE_API_KEY not set'}]
        headers = {'Accept': 'application/json', 'X-Subscription-Token': self.api_key}
        params = {'q': query, 'count': 5}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.base_url, headers=headers, params=params) as r:
                    if r.status == 200:
                        data = await r.json()
                        return [{'title': i.get('title',''), 'url': i.get('url',''), 'description': i.get('description','')} for i in data.get('web',{}).get('results',[])]
                    return [{'error': f'API error: {r.status}'}]
        except Exception as e:
            return [{'error': str(e)}]
