# Imports
import sys
from flask_migrate import Migrate
import graphene
from app import db
from app.schema.query import Query
from app.schema.mutation import Mutation
from flask_graphql import GraphQLView
from app.create_app import create_app

# initializing app
sys.path.append("./app")
app = create_app()
db.init_app(app)
migrate = Migrate(app, db)

schema = graphene.Schema(query=Query, mutation=Mutation)

with app.app_context():
    db.create_all()

app.add_url_rule(
    "/graphql-api",
    view_func=GraphQLView.as_view(
        "graphql", schema=schema, graphiql=True  # for having the GraphiQL interface
    ),
)


@app.route("/")
def index():
    return "<p><a href=/graphql-api> Go to graphql interface</a></p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
