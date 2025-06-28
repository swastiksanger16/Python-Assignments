import requests
import os

def get_movie_titles() -> list[str]:
    movie_lst=[]
    while(True):
        movie_lst.append(input("Enter Movie Title: "))
        ch=input("Add More y/n:")
        if ch.lower()=="n":
            break
    return movie_lst

def fetch_movie_data(titles:list[str]) -> list[dict]:
    data_list=[]
    mov_url="http://www.omdbapi.com/"
    for title in titles:
        params={
            "t":title,
            "apikey":"ea62c956"
        }
        res=requests.get(url=mov_url,params=params)
        data_list.append(res.json())
    return data_list

def save_to_csv(data,filename,append=False) -> None:
    """
    If append=True, data is added without overwriting the file.
    Header is only written if the file doesn't exist or append=False.
    """
    
    if not data:
        print("No data to write.")
        return

    file_exists = os.path.isfile(filename)
    mode = 'a' if append else 'w'

    all_keys = {}
    for item in data:
        for key in item.keys():
            all_keys[key] = None 
    all_keys = list(all_keys.keys())
    
    with open(filename, mode) as f:
        
        if not file_exists or not append:
            f.write(",".join(all_keys) + "\n")

        for item in data:
            row = []
            for key in all_keys:
                value = str(item.get(key, ""))
                value = value.replace(",", " ") 
                row.append(value)
            f.write(",".join(row) + "\n")

def main():
    file_name=f"{input('Enter File Name: ')}.csv"
    movie_list=get_movie_titles()
    data_list=fetch_movie_data(movie_list)
    save_to_csv(data_list,file_name,True)


if __name__=="__main__":
    main()