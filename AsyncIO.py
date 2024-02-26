import asyncio
from time import sleep

async def print1():
    await asyncio.sleep(2)
    print('print1 function')
    
async def print2():
    await asyncio.sleep(4)
    print('print2 function')

async def print3():
    await asyncio.sleep(6)
    print('print3 function')

async def main():
    # await print1()
    # await print2()
    # await print3()

    # They will execute parallely now  
    L = await asyncio.gather(
        print1(),
        print2(),
        print3(),
    )
    print(L)

    # Anothetr method -> Creating a tasks -> How to use this
    # task1 = asyncio.create_task(print1())

asyncio.run(main())