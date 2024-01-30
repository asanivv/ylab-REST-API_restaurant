from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from . import schemas, crud
from .database import get_db

menu_router = APIRouter()


@menu_router.get("/", response_model=List[schemas.Menu])
def get_menus(db: Session = Depends(get_db)):
    return crud.get_menus(db=db)


@menu_router.get("/{menu_id}/", response_model=schemas.Menu)
def get_menu_by_id(menu_id, db: Session = Depends(get_db)):
    menu = crud.get_menu_by_id(db=db, menu_id=menu_id)
    if menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    else:
        return menu


@menu_router.get("/{menu_id}/submenus/", response_model=List[schemas.SubMenu])
def get_submenus(menu_id, db: Session = Depends(get_db)):
    submenus = crud.get_submenus(db=db, menu_id=menu_id)
    return submenus


@menu_router.get("/{menu_id}/submenus/{submenu_id}/", response_model=schemas.SubMenu)
def get_submenu_by_id(menu_id, submenu_id, db: Session = Depends(get_db)):
    submenus = crud.get_submenu_by_id(db=db, menu_id=menu_id, submenu_id=submenu_id)
    if submenus is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    else:
        return submenus


@menu_router.get("/{menu_id}/submenus/{submenu_id}/dishes/", response_model=List[schemas.Dish])
def get_dishes(menu_id, submenu_id, db: Session = Depends(get_db)):
    dishes = crud.get_dishes(db=db, menu_id=menu_id, submenu_id=submenu_id)
    return dishes


@menu_router.get("/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}/", response_model=schemas.Dish)
def get_dish_by_id(menu_id, submenu_id, dish_id, db: Session = Depends(get_db)):
    dish = crud.get_dish_by_id(db=db, menu_id=menu_id, submenu_id=submenu_id, dish_id=dish_id)
    if dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    else:
        return dish


@menu_router.post("/", response_model=schemas.MenuCreate, status_code=201)
def create_menu(menu: schemas.MenuBase, db: Session = Depends(get_db)):
    db_menu = crud.get_menu_by_title(db=db, title=menu.title)
    if db_menu:
        raise HTTPException(status_code=400, detail="Title of Menu already registered")
    return crud.create_menu(db=db, menu=menu)


@menu_router.post("/{menu_id}/submenus/", response_model=schemas.SubMenuCreate, status_code=201)
def create_submenu(menu_id, submenu: schemas.MenuBase, db: Session = Depends(get_db)):
    db_menu = crud.check_menu_by_id(db=db, menu_id=menu_id)
    if not db_menu:
        raise HTTPException(status_code=400, detail="ID of Menu not registered")
    db_submenu = crud.get_submenu_by_title(db=db, title=submenu.title)
    if db_submenu:
        raise HTTPException(status_code=400, detail="Title of Submenu already registered")
    return crud.create_submenu(db=db, menu_id=menu_id, submenu=submenu)


@menu_router.post("/{menu_id}/submenus/{submenu_id}/dishes/", response_model=schemas.Dish, status_code=201)
def create_dish(menu_id, submenu_id, dish: schemas.DishCreate, db: Session = Depends(get_db)):
    db_menu = crud.check_menu_by_id(db=db, menu_id=menu_id)
    if not db_menu:
        raise HTTPException(status_code=400, detail="ID of Menu not registered")
    db_submenu = crud.check_submenu_by_id(db=db, submenu_id=submenu_id)
    if not db_submenu:
        raise HTTPException(status_code=400, detail="ID of Submenu not registered")
    return crud.create_dish(db=db, menu_id=menu_id, submenu_id=submenu_id, dish=dish)


@menu_router.patch("/{menu_id}/", response_model=schemas.Menu)
def update_menu(menu_id, menu: schemas.MenuBase, db: Session = Depends(get_db)):
    return crud.update_menu(db=db, menu_id=menu_id, menu=menu)


@menu_router.patch("/{menu_id}/submenus/{submenu_id}/", response_model=schemas.SubMenu)
def update_submenu(menu_id, submenu_id, submenu: schemas.MenuBase, db: Session = Depends(get_db)):
    return crud.update_submenu(db=db, menu_id=menu_id, submenu=submenu, submenu_id=submenu_id)


@menu_router.patch("/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}/", response_model=schemas.Dish)
def update_dish(menu_id, submenu_id, dish_id, dish: schemas.DishUpdate, db: Session = Depends(get_db)):
    return crud.update_dish(db=db, menu_id=menu_id, submenu_id=submenu_id, dish_id=dish_id, dish=dish)


@menu_router.delete("/{menu_id}/")
def delete_menu_by_id(menu_id, db: Session = Depends(get_db)):
    return crud.delete_menu_by_id(db=db, menu_id=menu_id)


@menu_router.delete("/{menu_id}/submenus/{submenu_id}/")
def delete_submenu_by_id(menu_id, submenu_id, db: Session = Depends(get_db)):
    return crud.delete_submenu_by_id(db=db, menu_id=menu_id, submenu_id=submenu_id)


@menu_router.delete("/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}/")
def delete_dish_by_id(menu_id, submenu_id, dish_id, db: Session = Depends(get_db)):
    return crud.delete_dish_by_id(db=db, menu_id=menu_id, submenu_id=submenu_id, dish_id=dish_id)
