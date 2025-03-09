import instaloader

loader = instaloader.Instaloader(
    download_comments=False,
    download_geotags=False,
    download_pictures=False,
    download_video_thumbnails=False,
    save_metadata=False
)
loader.load_session("", {
    "csrftoken": "",
    "sessionid": "",
    "ds_user_id": "",
    "mid": "",
    "ig_did": ""
})

profile = instaloader.Profile.from_id(loader.context, 3699211504).username
