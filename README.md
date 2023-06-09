# WebSocket Server

This is a WebSocket server implementation in Python using the `websockets` library. It allows clients to connect and exchange JSON messages.

## Requirements

- Python 3.7 or higher
- `websockets` library

## Getting Started

1. Install the required dependencies:
   ```bash
   $ pip install websockets

2. Start the server:

 $ python server.py

3. The server will start listening on the specified host and port (default: localhost:7889).
4. Clients can connect to the server using a WebSocket client library or framework of their choice.

## Server Details

The server uses asyncio to handle multiple client connections asynchronously.
When a client connects, it is added to the set of connected_clients.
The handle_client function is responsible for processing messages received from clients.
The received JSON message is parsed, and the player's ID, x-coordinate, and y-coordinate are extracted.
The game state is updated with the received coordinates, and the updated state is broadcasted to all connected clients.
The users list keeps track of the connected users and is updated whenever a new user joins the server.
