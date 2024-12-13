import yt_dlp
import os

#Get the downloads folder path
def resolvePathForDocker(outputPath):
    # Check if the path starts with the host's home directory
    host_home_dir = os.getenv("HOST_HOME", "/host/home")
    docker_home_dir = "/host/home"
    
    print(f"Host home directory: {host_home_dir}")
    
    if outputPath.startswith(host_home_dir):
        # Replace the host home directory with Docker's mapped directory
        return outputPath.replace(host_home_dir, docker_home_dir)
    
    return outputPath

#Main function
def youtube_to_mp3(url, outputPath):
    try:
        os.makedirs(outputPath, exist_ok=True)
        
        # Configure yt_dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(outputPath, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        # Download and convert video to mp3 using yt_dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("Download and conversion complete.")
        
        decision = input("Would you like to convert another video? (Y/N): ")
        
        if decision.lower() == 'n':
            exit()
            
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
#Main menu      
print("Welcome to the YouTube to MP3 converter!")
  
while True:
    url = input("Enter the YouTube video URL (Leave blank to exit): ")
    
    if not url:
        exit()
    
    outputPath = input("Enter the output path, leave blank for default (Downloads folder): ")
    
    if not outputPath:
        outputPath = "host/home/Downloads"
    else:
        outputPath = resolvePathForDocker(outputPath)
    
    
    youtube_to_mp3(url, outputPath)  
    
    