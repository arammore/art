import json
import random
from utils.ArtistClass import *
import pandas as pd
from pandas import read_excel

if __name__ == '__main__':
    df = DataReader('books/art_database.xlsx').df_generator()
    art = Art(df)
    random_mov_artist_1 = art.gen_random_mov_artist()
    random_mov_artist_2 = art.gen_random_mov_artist()

    artist1 = Artist(df, movement=random_mov_artist_1[0], artist=random_mov_artist_1[1])
    artist2 = Artist(df, random_mov_artist_2[0], random_mov_artist_2[1])

    print(artist1.access_to_artist_row())
    print(artist2.access_to_artist_row())

    compare = CompareArtists(data1=artist1.access_to_artist_row(), data2=artist2.access_to_artist_row())
    compare.compare_two()
