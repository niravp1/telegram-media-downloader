from telethon import TelegramClient, functions, errors
from dotenv import load_dotenv
import cryptg
from pathlib import Path
import os,asyncio

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
def callback(current, total):
    print('Downloaded', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))

async def main():
    link_for_channel = input("Type full link of the group: ")
    async with TelegramClient("session",api_id,api_hash) as client:
        try:
            channel = await client.get_entity(link_for_channel)
        except errors.BadRequestError:
            print("Not valid URL make sure to include https://")
            exit()
        download_directory = Path(input("Enter absolute download directory: "))

        #check if it channel topics, if not just download all media from channel from recent to oldest
        try:
            result = await client(functions.channels.GetForumTopicsRequest(channel,limit=100,offset_date=0, offset_id=0, offset_topic=0))
            await topic_getter(channel,client,result,download_directory)
        except:
           await downloader(client,channel,download_directory)


async def topic_getter(channel,client,result,download_directory):
    for topic in result.topics:
      print(f"ID: {topic.id} {topic.title} ")
    topic_id = int(input("Type ID of channel you want to download media from: "))
    await downloader(client,channel,download_directory,topic_id)

async def downloader(client,channel,download_directory,topic_id=None):
    tasks = []
    async for message in client.iter_messages(channel,reply_to=topic_id):
            task = asyncio.create_task(file_download_queue(client,message,download_directory))          
            tasks.append(task)
    await asyncio.gather(*tasks)

# semamphore has 10 slots to fill so downloads can simulate concurrency
async def file_download_queue(client,message,download_directory):
    sempahore = asyncio.Semaphore(10)
    async with sempahore:
      await client.download_media(message,download_directory, progress_callback=callback)

asyncio.run(main())
print("All files downloaded") 

"""
1. add error handling if channel is empty or message id doesn't exist etc
2. add documentation
3. add way to stop
"""