import strawberry


from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from controllers.buoys import Mutation, Query

from fastapi.middleware.cors import CORSMiddleware



schema = strawberry.Schema(Query,Mutation)


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# also inclue rest api here. But it's not necessary for this example
@app.get("/")
async def root():
    return {"message": "welcome to the server"}



app.include_router(graphql_app, prefix="/graphql")