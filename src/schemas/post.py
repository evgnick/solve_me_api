POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"}
    },
    "required": ["id"]
}

# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]

# POST_SCHEMA = {
#     "type": "object",
#     "properties": {
#         "id": {"type": "integer"},
#         "title": {"type": "string", "enum": ["POST"]} - если нам надо задать значения, то можем использовать enum
#     },
#     "required": ["id"]
# }
