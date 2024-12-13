from rembg import remove
import os

#Using Docker mapped path
def resolvePathForDocker(inputPath):
    # Check if the path starts with the host's home directory
    host_home_dir = os.getenv("HOST_HOME", "/host/home")
    docker_home_dir = "/host/home"
    
    print(f"Host home directory: {host_home_dir}")
    
    if inputPath.startswith(host_home_dir):
        # Replace the host home directory with Docker's mapped directory
        return inputPath.replace(host_home_dir, docker_home_dir)
    
    return inputPath

#Creates the output path
def getOutputPath(inputPath):
    baseName, extension = os.path.splitext(os.path.basename(inputPath))
    directory = os.path.dirname(inputPath)

    # Modify the base name
    newBaseName = baseName + "_without_background"

    # Combine the new name with the original extension
    newFileName = newBaseName + extension
    
    # Create the new full path
    newFilePath = os.path.join(directory, newFileName)

    return(newFilePath)
    
    

def remove_background(input_image_path, output_image_path):
    # Check if the input image exists
    if not os.path.isfile(input_image_path):
        print(f"Error: {input_image_path} does not exist or is not a file.")
        return
    
    # Open the input image
    with open(input_image_path, "rb") as img_file:
        input_image = img_file.read()
    
    # Remove the background
    output_image = remove(input_image)
    
    # Save the output image
    with open(output_image_path, "wb") as out_file:
        out_file.write(output_image)
    
    print(f"Background removed successfully. Image saved in {output_image_path}")
    
    decision = input("Would you like to remove the background of another image? (Y/N): ")
    
    if decision.lower() == 'n':
        exit()
        

#Main menu      
print("Welcome to the background remover!")
  
while True:
    inputPath = input("Please, type the path of the image you want to erase its background (Leave blank to exit): ").strip()
    
    if not inputPath:
        print("Exiting...")
        exit()

    # Resolve the path for Docker
    inputPath = resolvePathForDocker(inputPath)
    print(f"Resolved file path: {inputPath}")
            
                
    print("The image is going to be saved in the Downloads folder.")
    outputPath = getOutputPath(inputPath)
    
    remove_background(inputPath, outputPath)  
    
