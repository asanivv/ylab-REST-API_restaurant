import uuid

from sqlalchemy import Column, ForeignKey, String, Numeric
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship

from .database import Base


class Menu(Base):
    __tablename__ = "menus"
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True, index=True)
    description = Column(String, default='')
    children = relationship(
        "SubMenu",
        back_populates="parent",
        cascade="all, delete",
        passive_deletes=True,
    )


class SubMenu(Base):
    __tablename__ = "submenus"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True, index=True)
    description = Column(String, default='')
    menu_id = Column(UUID, ForeignKey("menus.id", ondelete="CASCADE"))
    parent = relationship("Menu", back_populates="children")
    children = relationship(
        "Dish",
        back_populates="parent",
        cascade="all, delete",
        passive_deletes=True,
    )


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(UUID, primary_key=True,default=uuid.uuid4)
    title = Column(String, unique=True, index=True)
    description = Column(String, default='')
    price = Column(Numeric(10, 2), default=0.00)
    submenu_id = Column(UUID, ForeignKey("submenus.id", ondelete="CASCADE"))
    parent = relationship("SubMenu", back_populates="children")
