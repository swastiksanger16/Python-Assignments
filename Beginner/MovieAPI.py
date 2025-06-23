import requests
import json

movie_url="http://www.omdbapi.com/"
my_api_key="ea62c956"

def store_data(data):
    file_name=f"{data['Title']}.txt"
    with open(file_name,"w") as f:
        json_str = json.dumps(data, indent=4) 
        f.write(json_str)
    print(f"File Saved with name {file_name}")
        

def fetch_data(params):
    try:
        res=requests.get(url=movie_url,params=params)
        store_data(res.json())
    except:
        print("Title Entered is Misspelled or Not Available!")
    

def main():
    while(True):
        title=input("Enter Movie Name: ")
        params={
            "t":title,
            "apikey":my_api_key
        }
        fetch_data(params)
        ch=input("Continue y/n: ")
        if(ch.lower()=="n"):
            break

 
if __name__ == "__main__":
    main()
