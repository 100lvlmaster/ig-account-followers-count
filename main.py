import csv
from fileoperations import clean_usernames, csv_to_list
from meta import get_followers_count


filename: str = "campaign-leads.csv"
existing_file: str = "campaign_leads_followers_count.csv"
offset = 2853


def main():
    users = csv_to_list(filename)
    users = clean_usernames(users)
    existing_list = csv_to_list(existing_file)
    users[0]["followers"] = ""
    keys = users[0].keys()
    if offset is not None and offset == 0:
        with open("new-" + filename, "a+") as file:
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            file.close()
        # Cross checck followers in the list
    for idx, user in enumerate(users):
        if idx <= offset:
            continue
        ig_username = user["ig_username"]
        user["followers"] = get_followers_count(
            username=ig_username, users=existing_list
        )
        with open("new-" + filename, "a+") as file:
            writer = csv.DictWriter(file, keys)
            writer.writerow(user)


if __name__ == "__main__":
    main()
