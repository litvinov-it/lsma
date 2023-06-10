# Imports
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from typing import List

# Init router
#     prefix - начальный префикс для дальнейших запросов
router = APIRouter(
    prefix='/posts'
)

# Create endpoints
#     response_model - тип данных ответа
#     status_code - 

@router.get('/', response_model=List[schemas.Post])
def get_posts(db: Session=Depends(get_db)):
    # Запрос к базе данных
    posts = db.query(models.Post).all()
    return posts

@router.get('/{id}', response_model=schemas.Post)
def get_post(id: int, db: Session=Depends(get_db)):
    # Запрос к базе данных
    post = db.query(models.Post).filter(models.Post.id == id).first()
    # Проверка найден ли пост
    if post is None:
        # Выкидываем ошибку
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f'post with id={id} was not found'
        )
    return post

@router.post('/', response_model=schemas.Post, status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session=Depends(get_db)):
    new_post = models.Post(**post.dict())
    # Add in db
    db.add(new_post)
    # Save in db
    db.commit()
    # Refresh in db
    db.refresh(new_post)
    return new_post

@router.put('/{id}', response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session=Depends(get_db)):
    # Сохранили запрос
    post_query = db.query(models.Post).filter(models.Post.id == id)

    if post_query.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f'post with id={id} was not found'
        )
    
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()

@router.delete('/{id}')
def delete_post(id: int, db: Session=Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    if post_query.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f'post with id={id} was not found'
        )
    
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)