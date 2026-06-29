import aiohttp

async def send_to_telegram(token, chat_id, message, topic_id=None):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown'}
    if topic_id:
        data['message_thread_id'] = int(topic_id)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as r:
                return await r.json() if r.status == 200 else None
    except:
        return None
