import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            json.load(file) #load all data from file and convert it to json
    except FileNotFoundError:
        return [] 
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print('*'*70)
    for index,video in enumerate(videos,start=1):
     
       print(f'{index}, {video}') 
    print('*' * 70) 

def add_youtube_video(videos):
    name=input("Enter the name of the video: ")
    time=input("Enter video time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
def update_youtube_video(videos):
     list_all_videos(videos)

     index = int(input("Enter video number to update: "))

     if 1 <= index <= len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")

        videos[index - 1]['name'] = name
        videos[index - 1]['time'] = time

        save_data_helper(videos)
        print("✅ Video updated successfully")
     else:
        print("❌ Invalid video number")

def delete_youtube_video(videos):
    list_all_videos(videos)

    index = int(input("Enter video number to delete: "))

    if 1 <= index <= len(videos):
        deleted_video = videos.pop(index - 1)
        save_data_helper(videos)
        print(f"🗑️ Deleted video: {deleted_video['name']}")
    else:
        print("❌ Invalid video number")    


def main():
    videos= load_data() 
    while True:
        print("\n Youtube Manager | Choose an option")
        print('1. List all youtube videos')
        print("2. Add youtube video")
        print("3. Update a youtube video details")
        print("4.Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_youtube_video(videos)
            case '3':
                update_youtube_video(videos)
            case '4':
                delete_youtube_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == '__main__': #agar function ka nam main h to main run krdo
    main()  #main entry point of this program
        