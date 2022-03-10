from instaloader import (
    Instaloader,
    LoginRequiredException,
    Profile,
    ProfileNotExistsException,
)

from fileoperations import clean_username

L = Instaloader(max_connection_attempts=1)


def get_followers_count(username: str):
    username = clean_username(username)
    profile: Profile
    try:
        profile = Profile.from_username(L.context, username)
    except LoginRequiredException:
        return "N/A"
    except ProfileNotExistsException as e:
        return "N/A"
    return profile.followers


# def get_followers_count(username: str, users: list) -> int:
#     cleaned_username = clean_username(username)
#     for user in users:
#         if user["Instagramhandle"] == cleaned_username:
#             return user["followers"]
#     L = Instaloader()
#     print(username)
#     profile: Profile
#     try:
#         profile = Profile.from_username(L.context, username)
#     except LoginRequiredException:
#         return "N/A"
#     except ProfileNotExistsException as e:
#         return "N/A"
#     return profile.followers
