app = Flask(__name__)

app.config['SECRET_KEY'] = 'hardsecretkey'

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flaskcodeloop:password@localhost/flaskcodeloop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False