import asyncio
from time import *

async def main(nm):
    nm = input("") 
    if nm == "ok":
        a = strftime('il est : %H:%M:%S')
        print(a)
        await asyncio.sleep(2)
        b = strftime('il est : %H:%M:%S')
        print(b)
        await asyncio.sleep(2)
        c = strftime('il est : %H:%M:%S')
        print(c)
    

asyncio.run(main(""))