import asyncio
from test import Test
from backtest import Backtest


async def main():
    bt = Backtest()
    await bt.fill_fyers()
    tt = Test(bt.fyers)
    await tt.user_fyers()


if __name__ == "__main__":
    asyncio.run(main())
