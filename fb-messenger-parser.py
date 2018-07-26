import os
import collections
import json
import datetime
import re

MessageResult = collections.namedtuple('MessageResult',
                                       'sender_name, timestamp_ms, content, title')


def main():
    if_case_sensitive = None
    matches = None

    base_dir = get_base_dir(input("Set the base directory for facebook messenger messages (exported as json): "))
    search_text = input("Search text: ")
    while not if_case_sensitive:
        if_case_sensitive = input("Should search be case sensitive? (y/n): ")
        if if_case_sensitive == 'y':
            matches = search_directories(search_text, base_dir, 0)
        elif if_case_sensitive == 'n':
            matches = search_directories(search_text, base_dir, 2)
        else:
            if_case_sensitive = None

    for m in matches:
        print('---------------------------')
        print('Message content: "{}"'.format(m.content))
        print('Sender name: {}'.format(m.sender_name))
        print('Timestamp: {}'.format(datetime.datetime.fromtimestamp(m.timestamp_ms / 1000).strftime(
            '%Y-%m-%d %H:%M:%S')))
        print('Conversation title: {}'.format(m.title))


def get_base_dir(directory):
    if not directory or not directory.strip():
        return None
    if not os.path.isdir(directory):
        return None
    return os.path.abspath(directory)


def search_directories(search, directory, case_sensitive=2):
    items = os.listdir(directory)
    for item in items:
        full_item = os.path.join(directory, item)
        if os.path.isdir(full_item):
            yield from search_directories(search, full_item, case_sensitive)
        elif item == 'message.json':
            yield from search_messages(search, full_item, case_sensitive)


def search_messages(search, file, case_sensitive):
    with open(file, 'r', encoding='utf-8') as fin:
        messages_data = json.load(fin)
        messages = messages_data.get('messages')
        title = messages_data.get('title')
        if not title:
            title = 'None'
        else:
            title = title.encode('iso-8859-1').decode('utf-8')
        for message in messages:
            sender_name = message.get('sender_name')
            timestamp_ms = message.get('timestamp_ms')
            content = message.get('content')
            if content and sender_name:
                content = content.encode('iso-8859-1').decode('utf-8')
                sender_name = sender_name.encode('iso-8859-1').decode('utf-8')
                # flag=0 -> case sensitive, flag=2 -> case insensitive
                if re.search(search, content, flags=case_sensitive):
                    message = MessageResult(sender_name=sender_name, timestamp_ms=timestamp_ms, content=content,
                                            title=title)
                    yield message


if __name__ == '__main__':
    main()
