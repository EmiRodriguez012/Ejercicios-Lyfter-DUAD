def read_songs(file_path):
    with open (file_path) as file:
        songs_list= file.readlines()
        return songs_list
    
def sort_songs(songs_list):
    songs_list.sort()
    return songs_list
        
def save_songs(file_path, songs_list):
    with open (file_path, "w") as file:
        for element in songs_list:
            file.write(element)

def print_songs(songs_list):
    for element in songs_list:
        print(F"Song: {element.strip()}")

def main():

    input_file = r"C:\Users\josue\Documents\nombre de canciones.txt"
    output_file = r"C:\Users\josue\Documents\canciones ordernadas alfabeticamente.txt"
    songs = read_songs(input_file)
    songs = sort_songs(songs)

    save_songs(output_file, songs)
    print_songs(songs)

main()