import csv
from fileoperations import clean_usernames, csv_to_list
from meta import get_followers_count


filename: str = "csv/campaign-leads.csv"
existing_file: str = ""
offset = 0


def main():
    users = csv_to_list(filename)
    existing_list = csv_to_list(existing_file)
    users[0]["followers"] = ""
    keys = users[0].keys()
    # Create csv and write csv if offset is 0
    if offset is not None and offset == 0:
        with open("csv/new-" + filename, "a+") as file:
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            file.close()
        # Cross checc followers in the list
    with open("csv/new-" + filename, "a+") as file:
        for idx, user in enumerate(users):
            if idx <= offset:
                continue
            username = user["Instagramhandle"]
            print(idx)
            print(username)
            user["followers"] = get_followers_count(
                username=username, users=existing_list
            )
            writer = csv.DictWriter(file, keys)
            writer.writerow(user)


if __name__ == "__main__":
    main()
