import csv

from meta import get_followers_count


def read_users_csv(filename: str):
    a_csv_file = open(filename, "r")
    data = csv.DictReader(a_csv_file)
    users = list(data)
    for user in users:
        ig_handle = user["Instagramhandle"]
        username = clean_username(ig_handle)
        user["ig_username"] = username
    return users


def write_users_csv(filename: str, data: list):
    keys = data[0].keys()
    a_file = open(filename, "a+")
    dict_writer = csv.DictWriter(a_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)
    a_file.close()


def clean_username(name: str) -> str:
    username: str = name.strip("@").strip("/")
    if name.startswith("http"):
        username = name.split("?")[0].strip("/").split("/")[-1]
    username = username.strip("@")
    return username
