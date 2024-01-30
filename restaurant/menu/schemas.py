import decimal
import uuid
from uuid import UUID

from pydantic import BaseModel, condecimal, ConfigDict, Field


class MenuBase(BaseModel):
    id: UUID = Field(default=uuid.uuid4)
    title: str
    description: str


class MenuCreate(MenuBase):
    model_config = ConfigDict(from_attributes=True)

    submenus_count: int
    dishes_count: int


class Menu(MenuBase):
    model_config = ConfigDict(from_attributes=True)

    submenus_count: int
    dishes_count: int


class SubMenu(MenuBase):
    model_config = ConfigDict(from_attributes=True)

    dishes_count: int


class SubMenuCreate(MenuBase):
    model_config = ConfigDict(from_attributes=True)

    dishes_count: int


class SubMenuUpdate(MenuBase):
    menu_id: UUID


class Dish(MenuBase):
    model_config = ConfigDict(from_attributes=True)

    price: condecimal(decimal_places=2)


class DishCreate(MenuBase):
    price: decimal.Decimal


class DishUpdate(MenuBase):
    price: decimal.Decimal
