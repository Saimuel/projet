import sys
from projet import db
from projet.models import User


def main(argv):
    if argv[0] == "createdb":
        db.create_all()

    if argv[0] == "deletedb":
        pass

    if argv[0] == "test":
        test_user = User(email='admin@example.com', password='test')
        db.session.add(test_user)
        db.session.commit()

    if argv[0] == "test2":
        users = User.query.all()
        print(users)

if __name__ == "__main__":
    main(sys.argv[1:])
