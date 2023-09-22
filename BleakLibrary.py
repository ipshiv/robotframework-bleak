from bleak import BleakClient
import asyncio
import threading
import platform

class BleakLibrary:
    def __init__(self) -> None:
        self.__client = None
        self.__loop = asyncio.get_event_loop()
        threading.Thread(target=self.runfunc).start()

    async def __dummy_main(self):
        while True:
            await asyncio.sleep(1)

    def runfunc(self) -> None:
        asyncio.run(self.__dummy_main())

    async def __connect(self, uuid):
        self.__client = BleakClient(uuid)
        await self.__client.connect()
        if self.__client.is_connected:
            if platform.system() != "Darwin":
                await self.__client.pair()

    async def __disconnect(self):
        await self.__client.disconnect()

    def connect(self, uuid) -> None:
        if not self.__client:
            self.__loop.run_until_complete(self.__connect(uuid))
            return self.__client.is_connected
        else:
            print("Already connected")
            return True

    def disconnect(self) -> None:
        if self.__client:
            self.__loop.run_until_complete(self.__disconnect())
            self.__client = None
            return True
        else:
            return False
