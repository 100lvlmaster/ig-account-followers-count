import csv
from fileoperations import read_users_csv, write_users_csv
from meta import get_followers_count

file: str = "campaign-leads.csv"


def main():
    users = read_users_csv(file)

    for user in users:
        ig_username = user["ig_username"]
        user["followers"] = get_followers_count(ig_username)
        break
    # for user in users:
    write_users_csv(filename="new-" + file, data=users)


if __name__ == "__main__":
    main()
