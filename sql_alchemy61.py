# 传说中的ORM技术

# 第一步，导入SQLAlchemy，并初始化DBSession：

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey
from collections import Iterable
from  sqlalchemy.types import INTEGER

# 创建对象的基类
Base = declarative_base()

class Books(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))

# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(60))
    books = relationship('Books')



# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/lmtest') # create_engine()用来初始化数据库连接。

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 以上代码完成SQLAlchemy的初始化和具体每个表的class定义。如果有多个表，就继续定义其他class，例如School




# 由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象
# 创建session对象:
session = DBSession()
# # # 创建新User对象:
# # new_user = User(id='5', name='lm')
# book = Books(id = 2, name = 'yoyo', user_id = 5)
# # # 添加到session:
# session.add(book)
#
#
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()

# 可见，关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。



# 如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是tuple，而是User对象。

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id==5).one()

# 打印类型和对象的name属性:
print(isinstance(user.books, Iterable))
print(len(user.books))

# print([k+y for k, y in user.books[]])
print(user.books[0].id)
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()



# 可见，ORM就是把数据库表的行与相应的对象建立关联，互相转换。
#
# 由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能

# 例如，如果一个User拥有多个Book，就可以定义一对多关系如上：


