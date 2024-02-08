import instaloader

def download_profile_pictures(profile_name):
    loader = instaloader.Instaloader()
    
    try:
        profile = instaloader.Profile.from_username(loader.context, profile_name)
        
        for post in profile.get_posts():
            loader.download_post(post, target=profile_name)
            
            print(f"All pictures from profile '{profile_name}' download succesfully")
            
    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error: {e}")
        

if __name__ == "__main__":
    
    profile_name = "Write The Profile Name Here"
    
    download_profile_pictures(profile_name)