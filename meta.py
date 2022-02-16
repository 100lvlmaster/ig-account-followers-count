from instaloader import (
    Instaloader,
    LoginRequiredException,
    Profile,
    ProfileNotExistsException,
)


def get_followers_count(username: str) -> int:
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
