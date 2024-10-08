from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

import database, schemas, models, utils, oauth2

router = APIRouter(tags=["Authentication"])

# Passing the user credentials in built-in fastapi module
@router.post('/login', response_model=schemas.Token)
# instead of the below code, we will make it better by using the oauth2 module
# def login(user_credentials: schemas.UserLogin, db: Session = Depends(database.get_db)):
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    
    {
        "username": "meh",       #user_credentials.username,
        "password": "hehe"      #user_credentials.password
    }
    user = db.query(models.User).filter(
        models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    # Create a Token
    # Return token
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    
    # return {"token":"example token"}
    return {"access_token" : access_token, "token_type" : "bearer"}
    
    