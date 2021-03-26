import os
import re
import cv2


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


def move_images(experiment_name, destination_folder, folder=None, extension="png", move=True):
    if not folder:
        folder = get_download_path()

    files = [f for f in os.listdir(folder) if
             re.match(r'{experiment_name}[0-9]+.{extension}'.format(experiment_name=experiment_name,
                                                                    extension=extension), f)]
    images_paths = []

    for file in files:
        current_path = os.path.join(folder, file)
        destination_path = os.path.join(destination_folder, file)
        if move:
            os.rename(current_path, destination_path)
        images_paths.append(destination_path)
    return images_paths


def create_video(experiment_name, images_paths, destination_folder, index_start_video=3):
    # sort images paths
    images_paths = sorted(images_paths, key=lambda im: int(im.split("\\")[-1].split(".")[0].replace(experiment_name, "")))

    print("init video")
    video_name = os.path.join(destination_folder, '{experiment_name}.avi'.format(experiment_name=experiment_name))

    # get data from first image to determine frame characteristics
    frame = cv2.imread(images_paths[0])
    height, width, layers = frame.shape

    print("cv2 video writer video")
    video = cv2.VideoWriter(video_name, 0, 10, (width, height))

    for i, image in enumerate(images_paths):
        print(i)
        if i >= index_start_video:
            if i % 5 == 0:
                video.write(cv2.imread(image))

    cv2.destroyAllWindows()
    video.release()


if __name__ == "__main__":

    experiment_name = "monsters"
    extension = "png"
    destination_folder = ""

    images_paths = move_images(experiment_name=experiment_name,
                               destination_folder=destination_folder,
                               folder=destination_folder,
                               extension=extension,
                               move=False)
    index_start_video = 7
    create_video(experiment_name=experiment_name,
                 images_paths=images_paths,
                 destination_folder=destination_folder,
                 index_start_video=index_start_video)

    # todo: add text to video