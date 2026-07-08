import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def data_saver_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def list_videos(videos):
    print("\n")
    print("*"*20)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} is {video['time']} long")
    print("*"*20)
    print("\n")


def add_video(videos):
    name = input("Name of Video: ")
    time = input("Time of Video: ")
    videos.append({'name':name, 'time':time})
    data_saver_helper(videos)


def delete_video(videos):
    list_videos(videos)
    index = int(input("Tell the video number you want to delete: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        data_saver_helper(videos)
    else:
        print("Invalid Request!!")
    list_videos(videos)


def update_video(videos):
    list_videos(videos)
    index = int(input("Tell the video number you want to update: "))
    if 1<= index <= len(videos):
        name = input("Name of the New Video: ")
        time = input("Time of the New Video: ")
        videos[index-1] = {'name':name, 'time':time}
        data_saver_helper(videos)
    else:
        print("Invalid Request!!")
    list_videos(videos)
        

def main():
    videos = load_data()
    while True:
        print("YT Manager || Choose An Option!")
        print("1. List All Videos")
        print("2. Add A Video")
        print("3. Delete A Video")
        print("4. Update A Video")
        print("5. Exit The App")
        choice = input("Enter Your Choice: ")

        match choice:
            case '1':
                list_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                delete_video(videos)
            case '4':
                update_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice!!")


if __name__ == "__main__":
    main()
