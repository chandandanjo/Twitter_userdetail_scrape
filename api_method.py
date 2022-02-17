import requests

bearer_token = input("Enter your bearer token obtained from Twitter developer account : ")
twitter_url = input("Enter twitter profile url: ")
username = twitter_url[20:]
url = f'https://api.twitter.com/2/users/by/username/{username}?user.fields=id,description,public_metrics'
header = {'Authorization': f'Bearer {bearer_token}'}
response = requests.request('GET', url, headers=header)
initial_dict = response.json()['data']
output_initial_dict = {'biography': initial_dict['description'],
                       'followers_count': initial_dict['public_metrics']['followers_count'],
                       'following_count': initial_dict['public_metrics']['following_count'],
                       'likes_count': initial_dict['public_metrics']['listed_count'], 'user_id': initial_dict['id']}

print(output_initial_dict)
