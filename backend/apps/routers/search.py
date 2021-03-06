from typing import List

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from database import get_db

from .. import schemas
from ..repository import search

router = APIRouter(
    prefix="/search",
    tags=["searches"],
)


@router.post("/category", response_model=schemas.SearchResult)
def search_category(request: schemas.SearchCategory, db: Session = Depends(get_db)):
    return search.get_product_by_category(db, request)


@router.post("/keyword", response_model=schemas.SearchResult)
def search_keyword(request: schemas.SearchKeyword, db: Session = Depends(get_db)):
    return search.get_product_by_keyword(db, request)


@router.post("/keyword/autocomplete", response_model=schemas.KeywordAutocompleteList)
def get_keyword_autocomplete(request: schemas.Keyword, db: Session = Depends(get_db)):
    return search.get_keyword_autocomplete(db, request)


@router.post("/ingredient", response_model=schemas.SearchResult)
def search_ingredient(
    request: schemas.SearchIngredients, db: Session = Depends(get_db)
):
    return search.get_product_by_ingredient(db, request)


@router.post(
    "/ingredient/autocomplete", response_model=schemas.IngredientAutocompleteList
)
def get_ingredient_autocomplete(
    request: schemas.Keyword, db: Session = Depends(get_db)
):
    return search.get_ingredient_autocomplete(db, request)
