import asyncio
from utils.database_api.db_publicplaces import db
from utils.database_api import quick_commands
from data import config

async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    # await db.gino.drop_all()
    await db.gino.create_all()

    await quick_commands.add_user(11, 'V')
    await quick_commands.add_user(12, 'Va')
    await quick_commands.add_user(13, 'Vag')
    await quick_commands.add_user(14, 'Vage')

    await quick_commands.add_pp(1,'Good','89537975555','52131231,51231231','Good public','12-22','Поесть','blob','vk.com',4.25)

    users = await quick_commands.select_all_users()
    print(users)

    count = await quick_commands.count_users()
    print(count)

    user = await quick_commands.select_user(11)
    print(user)

    await quick_commands.delete_user(11)
    user = await quick_commands.select_user(11)
    print(user)

    await quick_commands.update_user(12, 'Ivan')
    user = await quick_commands.select_user(11)
    print(user)
