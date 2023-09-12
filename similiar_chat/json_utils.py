# -*- coding:utf-8 -*-
import os
import re
import json

path = "./similiar_chat/logs.txt"


def dump_query_dialogue_context(data):
    # path = os.path.join(LOGS_DIR, '{}.json'.format(str(user)))
    with open(path, 'w', encoding='utf8') as f:
        f.write(data)


def load_query_dialogue_context():
    with open(path, 'r', encoding='utf8') as f:
        data = f.read()
        return data


def delete_context():
    with open(path, 'w', encoding='utf8') as f:
        f.truncate(0)

