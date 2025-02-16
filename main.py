"""
Phone Number Generator Script
Author: Joel D'costa
GitHub: https://github.com/joelshanky
Date: 2025-02-16
Description: This script generates random phone numbers based on a given 
country code and starting digits. It exports the numbers as a VCF contact file.
"""

from keep_alive import keep_alive
import requests
import os
import sys
import time

keep_alive()
# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '000000000:XXXXXXXX0XXXXXXXXXXXXXX_XXXXXXX0X'


def get_chat_id(update):
  return update['message']['chat']['id']


def send_message(chat_id, text):
  url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
  params = {'chat_id': chat_id, 'text': text}
  response = requests.post(url, params=params)
  return response.json()


def send_document(chat_id, document_path):
  url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'
  files = {'document': open(document_path, 'rb')}
  params = {'chat_id': chat_id}
  response = requests.post(url, params=params, files=files)
  return response.json()


def remove_lines(filename):
  with open(filename, 'r') as file:
    lines = file.readlines()

  # Remove lines consisting only of equal signs
  lines = [
      line.strip() for line in lines if line.strip() != "=" * len(line.strip())
  ]

  with open(filename, 'w') as file:
    file.write('\n'.join(lines))


def handle_message(update):
  chat_id = get_chat_id(update)
  message_text = update['message']['text']
  send_message(chat_id, f'{message_text}')

  # Splitting the message_text into parts using "|"
  message_parts = message_text.split("|")

  # Checking if there are at least two parts in the list
  if len(message_parts) >= 2:
    code_1 = message_parts[0]
    code_2 = message_parts[1]

    # Execute your command with code_1 and code_2
    os.popen(f'python "test.py" "{code_1}" "{code_2}"')
    time.sleep(3)

    file_path = 'qwertx_contact_list.vcf'
    remove_lines(file_path)
    time.sleep(3)
    send_document(chat_id, file_path)
  else:
    # Handle the case where there are not enough parts in the message_text
    print("Not enough parts in the message_text")


def main():
  offset = None
  while True:
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    params = {'offset': offset}
    response = requests.get(url, params=params)
    data = response.json()

    for update in data['result']:
      if 'message' in update:
        handle_message(update)
      offset = update['update_id'] + 1


if __name__ == '__main__':
  main()
