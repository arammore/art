from os import listdir
from os.path import isfile, join
import random
from PIL import Image
import pandas as pd


class DataReader:
    def __init__(self, path):
        self.path = path

    def df_generator(self):
        data = pd.read_excel(self.path, sheet_name=0, header=0,
                             converters={'Año nacimiento': int, 'Año muerte': int})

        df = pd.DataFrame(data).fillna(0)
        df['Murió con'] = df['Año muerte'] - df['Año nacimiento']

        return df


class Art:
    def __init__(self, df):
        self.df = df

    def list_of_movements(self):
        return self.df["Movimiento"].unique()

    def artist_in_movements(self, movement):
        return list(self.df[movement].keys())

    def gen_random_mov_artist(self):
        random_movement = random.choice(self.list_of_movements())
        random_artist = random.choice(list(self.df[self.df['Movimiento'] == random_movement]['Artista']))

        return random_movement, random_artist


class Artist(Art):
    def __init__(self, df, movement, artist):
        super().__init__(df)
        self.movement = movement
        self.artist = artist

    def access_to_artist_row(self):
        df_artist = self.df[(self.df['Movimiento'] == self.movement) & (self.df['Artista'] == self.artist)]
        return df_artist

    def show_info(self):
        row = self.access_to_artist_row()
        print(f"Artist name: {row['Artista'].values[0]}")

    def access_to_image(self):
        path = f"works/{self.movement}/{self.artist}/"

        files_in_path = [f for f in listdir(path) if isfile(join(path, f))]
        if files_in_path:
            Image.open(path + random.choice(files_in_path)).show()
        else:
            print("Aún no tenemos obras de este artista")


class CompareArtists:
    def __init__(self, data1, data2):
        self.artist_1 = data1['Artista'].values[0]
        self.artist_2 = data2['Artista'].values[0]
        self.birth_date_1 = data1['Año nacimiento'].values[0]
        self.death_date_1 = data1['Año muerte'].values[0]
        self.birth_date_2 = data2['Año nacimiento'].values[0]
        self.death_date_2 = data2['Año muerte'].values[0]

    def compare_two(self):
        if self.birth_date_1 > self.birth_date_2:
            print(f"{self.artist_1} nació después que {self.artist_2}, {self.birth_date_1 - self.birth_date_2} años")
            if self.death_date_1 > self.death_date_2:
                print(f"Ambos artistas han coincidido entre {self.birth_date_1}-{self.death_date_2}, "
                      f"un total de {self.death_date_2 - self.birth_date_1} años")
            else:
                print(f"Ambos artistas han coincidido en {self.birth_date_1}-{self.death_date_1}, "
                      f"un total de {self.death_date_1 - self.birth_date_1} años")
        else:
            print(
                f"El artista {self.artist_2} nació después que {self.artist_1}, {self.birth_date_2 - self.birth_date_1} años")
            if self.death_date_1 > self.death_date_2:
                print(f"Ambos artistas han coincidido entre {self.birth_date_2}-{self.death_date_2}, "
                      f"un total de {self.death_date_2 - self.birth_date_2} años")
            else:
                print(f"Ambos artistas han coincidido entre {self.birth_date_2}-{self.death_date_1}, "
                      f"un total de {self.death_date_1 - self.birth_date_2} años")
