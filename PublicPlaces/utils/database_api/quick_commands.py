from asyncpg import UniqueViolationError
from utils.database_api.schemas.user import User
from utils.database_api.schemas.publicplace_base import PubliPlace
from utils.database_api.db_publicplaces import db


async def add_pp(pp_id: int, pp_name: str, ph_number: str, 
                 loc: str, atl: str, wt: str, ct: str, ph: str, 
                 link: str, rating: float):
    try:
        pp = PubliPlace(pp_id=pp_id, pp_name=pp_name, phone_number=ph_number,
                        location=loc,atl=atl,work_time=wt,category=ct,photo=ph,
                        link=link, rating=rating)
        await pp.create()
    except UniqueViolationError:
        print('Общественное место не добавлено') 




async def add_user(user_id: int, name: str):
    try:
        user = User(user_id=user_id, name=name)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен') 


async def select_all_users():
    users = await User.query.gino.all()
    return users

async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count

async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user

async def delete_user(user_id):
    user_del = await select_user(user_id)
    await user_del.delete()

async def update_user(user_id, new_name):
    upd_user = await select_user(user_id)
    await upd_user.update(name=new_name).apply()