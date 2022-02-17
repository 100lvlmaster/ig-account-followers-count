from instaloader import (
    Instaloader,
    LoginRequiredException,
    Profile,
    ProfileNotExistsException,
)

from fileoperations import clean_username


def get_followers_count(username: str, users: list) -> int:
    cleaned_username = clean_username(username)
    for user in users:
        if user["Instagramhandle"] == cleaned_username:
            print("already exists")
            return user["followers"]
    L = Instaloader()
    print(username)
    profile: Profile
    try:
        profile = Profile.from_username(L.context, username)
    except LoginRequiredException:
        return "N/A"
    except ProfileNotExistsException as e:
        return "N/A"
    return profile.followers
