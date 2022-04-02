from discord import Client


class MyBot(Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")