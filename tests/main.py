
import asyncio
from .tests import stress_test

async def run_stress_test():
    await stress_test(100, sleep=0.05)

if __name__ == "__main__":
    asyncio.run(run_stress_test())