import json

def stream():
    with open('./dataset/arxiv_data.json') as f:
        for line in f:
            data = json.loads(line)
            yield data

