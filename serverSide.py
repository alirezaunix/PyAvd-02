# serverSide.py (example of an async server)
import asyncio

async def start_server():
    # Example of an async server using asyncio
    async def handle_client(reader, writer):
        data = await reader.read(100)
        message = data.decode()
        #print(f"Received: {message}")
        writer.write(data)
        await writer.drain()
        writer.close()
        return message
    
    server = await asyncio.start_server(handle_client, '192.168.216.10', 65432)
    async with server:
        await server.serve_forever()