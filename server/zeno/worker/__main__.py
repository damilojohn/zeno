from typing import Literal
from fire import Fire
from zeno.worker.search import SearchWorker


RunType = Literal["search_agent"]


async def run_worker(type: RunType):
    if type == "search_agent":
        await SearchWorker().run()


if __name__ == "__main__":
    Fire(run_worker)
