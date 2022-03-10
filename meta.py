import code
import time
from urllib.error import HTTPError
from instaloader import (
    Instaloader,
    LoginRequiredException,
    Profile,
    ProfileNotExistsException,
)

from fileoperations import clean_username


def get_followers_count(username: str, users: list = []) -> int:
    cleaned_username = clean_username(username)
    L = Instaloader(max_connection_attempts=1)
    print(cleaned_username)
    if len(users) == 0:
        for user in users:
            if user["Instagramhandle"] == cleaned_username:
                return user["followers"]
    profile: Profile
    try:
        profile = Profile.from_username(L.context, username)
    except LoginRequiredException:
        return "Private"
    except ProfileNotExistsException as e:
        return "N/A"
    except HTTPError as e:
        time.sleep(20)
        return get_followers_count(username, users)

    return profile.followers
