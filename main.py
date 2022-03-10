import csv
from os.path import join
from fileoperations import clean_usernames, csv_to_list
from meta import get_followers_count


text_input = input("Enter offset (default=0) :\n")
offset = 0 if text_input is None or text_input == "" else int(text_input)

limit_text_input = input("Enter limit (default= end-of-list) :\n")
limit = (
    0 if limit_text_input is None or limit_text_input == "" else int(limit_text_input)
)

export_dir = "csv"
filename: str = "campaign-leads.csv"
existing_file: str = ""


def main():
    users = csv_to_list(filename)
    existing_list = csv_to_list(existing_file)
    users[0]["followers"] = ""
    keys = users[0].keys()
    export_file = join(export_dir, filename)
    # Create csv and write csv if offset is 0
    if offset is not None and offset == 0:
        with open(export_file, "a+") as file:
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            file.close()
        # Cross checc followers in the list
    with open(export_file, "a+") as file:
        for idx, user in enumerate(users):
            if limit != 0:
                if idx >= limit:
                    break
            if idx < offset:
                continue
            username = user["Instagramhandle"]
            print(idx)
            user["followers"] = get_followers_count(
                username=username, users=existing_list
            )
            writer = csv.DictWriter(file, keys)
            writer.writerow(user)
    file.close()


if __name__ == "__main__":
    main()
