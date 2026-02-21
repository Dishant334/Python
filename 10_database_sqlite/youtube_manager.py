import sqlite3
con=sqlite3.connect('youtube_videos.db')
cursor=con.cursor()
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS videos(
         id INTEGER PRIMARY KEY,
         name TEXT NOT NULL,
        time text NOT NULL
                     )
''')

def list_videos(videos):
    cursor.execute("SELECT * from videos")
    for row in cursor.fetchall():
        print(row)

def add_videos():
    name=input("Enter the name: ")
    time=input("Enter the time: ")
    cursor.execute('INSERT INTO  videos(name,time) Values (?,?)',(name,time))
    con.commit()
def update_videos(video):
    new_name=input("Enter the name: ")
    new_time=input("Enter the time: ")
    cursor.execute("UPDATE videos set name=? time=? where id=?",(new_name,new_time,video))
    con.commit()
def delete_videos(video):
    cursor.exectue("DELETE from videos where id=?",(video ,))
    con.commit()


def main():
    videos=[]
    while True:
        print("\n Youtube manager app with DB")
        print('1. List all youtube videos')
        print("2. Add youtube video")
        print("3. Update a youtube video details")
        print("4.Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice ")

        if choice=='1':
            list_videos(videos)
        elif choice=='2':
            add_videos()
        elif choice=='3':
            video= input("Enter video ID to update: ")
            update_videos(video)
        elif choice=='4':
            video=input("Enter videoId to delete: ")
            delete_videos(video)
        elif choice=='5':
            break
        else:
            print("Invalid Choice")

    con.close()

if __name__ =='__main__':
    main()