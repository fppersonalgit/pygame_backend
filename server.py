import asyncio
import websockets
import json


# Constants
PORT = 7889
MAX_PLAYERS = 10
SESSION = []
HOST = 'localhost'

connected_clients = set()
users = []

async def handle_client(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Receive the JSON string from the client
            data = json.loads(message)
            print(data)

            # Extract player's ID, x-coordinate, and y-coordinate
            player_id = data['player_id']
            x = data['x']
            y = data['y']
            print(player_id, x, y)
            # Update the game state with the received coordinates

            # Broadcast the updated game state to all connected clients
            updated_state = {
                "player_id": player_id,
                "x": x,
                "y": y
            }
            for client in connected_clients:
                await client.send(json.dumps(updated_state))
                print(client)

            if updated_state not in users:
                users.append(updated_state)
                print(f"Connected users: {users}")

    finally:
        connected_clients.remove(websocket)


async def main():
    server = await websockets.serve(handle_client, HOST, PORT)
    print(server)
    await server.wait_closed()


asyncio.run(main())
