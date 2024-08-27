"""In this file initialize
the dispatcher instance, to avoid circular imports in future
"""

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

dp = Dispatcher(storage=MemoryStorage())
