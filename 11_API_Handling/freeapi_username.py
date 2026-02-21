import requests

def fetch_random_user_freeapi():
    url='https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response=requests.get(url)
    data=response.json()
    
    if(data['success']):
        user=data['data']['login']['username']
        country=data['data']['location']['country']
        return user, country
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
       fetch_random_user_freeapi()
    except Exception as e:
        print(str(e))
        


if __name__=='__main__':
    main()