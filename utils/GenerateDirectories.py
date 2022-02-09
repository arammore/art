import os


def generate_directories(data_json):
    for corriente in list(data_json.keys()):
        path = f"obras/{corriente}/"

        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)

        for artist in list(data_json[corriente].keys()):
            artist_path = f"obras/{corriente}/{artist}/"
            try:
                os.mkdir(artist_path)
            except OSError:
                print("Creation of the directory %s failed" % artist_path)
            else:
                print("Successfully created the directory %s " % artist_path)

            print("-------")
        print("*" * 50)
