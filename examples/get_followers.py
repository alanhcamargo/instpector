from sys import argv
from context import Instpector, endpoints

def get_followers(**options):
    instpector = Instpector()
    if not instpector.login(user=options.get("user"), password=options.get("password")):
        return

    followers = endpoints.factory.create("followers", instpector)

    for follower in followers.of_user(options.get("target_user_id")):
        print(follower)

    instpector.logout()

if __name__ == '__main__':
    if len(argv) < 6:
        print((
            "Missing arguments: "
            "--user {user} "
            "--password {password} "
            "--target_user_id {user_id}"
        ))
        exit(1)
    get_followers(
        user=argv[2],
        password=argv[4],
        target_user_id=argv[6]
    )
