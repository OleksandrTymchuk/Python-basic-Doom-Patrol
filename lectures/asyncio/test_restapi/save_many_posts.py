import asyncio
from aiohttp_get import aiohttp_get_json
import json


async def save_posts(post_info):
    print('saving...')
    file = open('posts/post-'+ str(post_info['id']) + '.json', 'w')
    file.write(json.dumps(post_info))
    file.close()
    print('EndSaving')


async def get_posts(id):
    print('Start getting info for post #' + str(id))
    response = await aiohttp_get_json('https://jsonplaceholder.typicode.com/posts' + str(id))
    print('Start saving info for post #' + str(id))
    await save_posts(response)
    print('End')


async def main():
    file = open('posts.json', 'r')
    posts = json.loads(file.read())
    file.close()
    tasks = [get_posts(post['id']) for post in posts]
    await asyncio.gather(*tasks)

asyncio.run(main())
