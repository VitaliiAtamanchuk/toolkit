import os.path

from sqlalchemy import Column, DateTime, Integer, Sequence, String, Text, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, Sequence('msg_id_seq'), primary_key=True, nullable=False)
    username = Column(String(40), nullable=False)
    message = Column(Text)
    timestamp = Column(DateTime(), server_default=func.now(), nullable=False)


class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, Sequence('prj_id_seq'), primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)
    path = Column(Text, nullable=False)
    timestamp = Column(DateTime(), server_default=func.now(), nullable=False)

    @staticmethod
    async def create(request, path: str):
        async with request.app['pg_engine'].acquire() as conn:
            await conn.execute(sa_projects.insert().values(
                name=os.path.basename(path),
                path=path,
            ))
    
    @staticmethod
    async def all(request):
        retval = []
        async with request.app['pg_engine'].acquire() as conn:
            async for row in conn.execute(sa_projects.select()):
                retval.append({
                    'id': row.id,
                    'name': row.name,
                    'path': row.path
                })
        return retval
    
    @staticmethod
    async def delete(request, id):
        async with request.app['pg_engine'].acquire() as conn:
            query = sa_projects.delete().where(sa_projects.c.id==id)
            await conn.execute(query)
    
    @staticmethod
    async def get_path(request, id) -> str:
        # TODO: how to make scalar query?
        async with request.app['pg_engine'].acquire() as conn:
            query = (
                sa_projects.select()
                .where(sa_projects.c.id==id)
            )
            resultProxy = await conn.execute(query)
            path = (await resultProxy.fetchone()).path
        return path


sa_messages = Message.__table__
sa_projects = Project.__table__
