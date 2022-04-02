from asyncio import events
from os import name
import re
from telethon import TelegramClient, events, hints
from telethon.tl.functions.channels import JoinChannelRequest
import time
from telethon.tl.functions.messages import SendMessageRequest
import os

api_id = 8763319
api_hash = '28f53a40a4052cd950dab693a3a3c04c'

try:
    setup = open('setup.txt','r',encoding='utf-8').read().split('||')
    question = []
    answer = []
    for question_and_answer in setup:
        question.append(question_and_answer.split('|')[0])
        answer.append(question_and_answer.split('|')[1])
    
    print('Load thành công câu hỏi và câu trả lời !!!')
except:
    print('Lỗi đọc câu hỏi và câu trả lời . Vui lòng kiểm tra lại !!!!')
    time.sleep(100)

client = TelegramClient('admin', api_id, api_hash)
@client.on(events.NewMessage())
async def handler(event):
    text = event.message.raw_text
    if text in question:
        n = question.index(text)
        await event.reply(answer[n])
        print('--------------------------------Đã Rep--------------------------------')
        print(text)
        print('------------------------Hoàng Đẹp Trai VCL!!!--------------------------')
        print('\n\n\n')
    else:
        print('-------------------------------Không Rep-------------------------------')
        print(text)
        print('------------------------Hoàng Đẹp Trai VCL!!!--------------------------')
        print('\n\n\n')
client.start()
client.run_until_disconnected()