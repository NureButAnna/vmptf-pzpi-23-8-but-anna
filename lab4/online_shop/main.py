from fastapi import FastAPI
from app.api.v1.users import router as user_router
from app.api.v1.orders import router as order_router
from app.api.v1.products import router as product_router
from app.api.v1.reviews import router as review_router
from app.api.v1.categories import router as category_router
from app.api.v1.auth import router as auth_router
from fastapi.responses import Response

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(order_router)
app.include_router(product_router)
app.include_router(category_router)
app.include_router(review_router)

@app.get("/health")
def health_check():
    return Response(status_code=200)




