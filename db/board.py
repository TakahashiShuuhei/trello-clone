from google.cloud import datastore
client = datastore.Client(namespace='trello-clone')


def get(board_id):
    key = client.key('Board', board_id)
    return client.get(key)


def create(board):
    key = client.key('Board')
    entity = datastore.Entity(key=key)
    entity.update(board)
    client.put(entity)
    entity['id'] = entity.key.id
    return entity


def update(board_id, board):
    key = client.key('Board', board_id)
    entity = client.get(key)
    entity.update(board)
    client.put(entity)
    return entity


def delete(board_id):
    key = client.key('Board', board_id)
    client.delete(key)

