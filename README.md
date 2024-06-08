Codicent Python Library
=======================

This library provides a Python interface to the Codicent API.

### Installation
------------
To install using pip, run:
```bash
pip install git+https://github.com/izaxon/codicent-py.git
```

To use this library, simply import it into your Python script:
```python
from codicentpy import Codicent
```

### Usage
-----

### Initialization

Create a `Codicent` object with your API token and optional SignalR host:
```python
codicent = Codicent("YOUR_API_TOKEN")
```
### Uploading a File

Upload a file to Codicent:
```python
file_id = codicent.upload(open("example.txt", "rb"))
print(file_id)
```
### Posting a Message

Post a message to Codicent:
```python
message_id = codicent.post_message("Hello, world!", type="info")
print(message_id)
```
### Getting Messages

Get a list of messages from Codicent:
```python
messages = codicent.get_messages(start=0, length=10)
print(messages)
```
Methods
-------

### `__init__`

Initialize the `Codicent` object with a Codicent API token.

### `upload`

Upload a file to Codicent.

* `file`: The file to upload.

Returns the ID of the uploaded file.

### `post_message`

Post a message to Codicent.

* `message`: The message to post.
* `parent_id`: The ID of the parent message (optional).
* `type`: The type of message (default: "info").

Returns the ID of the posted message.

### `get_messages`

Get a list of messages from Codicent.

* `start`: The starting index (default: 0).
* `length`: The number of messages to retrieve (default: 10).
* `search`: A search query (optional).
* `after_timestamp`: A timestamp to retrieve messages after (optional).
* `before_timestamp`: A timestamp to retrieve messages before (optional).

Returns a list of message objects.
