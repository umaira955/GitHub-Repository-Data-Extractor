import requests
import csv

topic = input("Enter a topic: ")
found = False
try:
    response = requests.get(
        "https://api.github.com/search/repositories",
        params={"q": topic, "sort": "stars"} , timeout= 10
    )

except requests.RequestException as e:
    print(f"Request failed: {e}")
    exit()

if response.status_code == 200:
    data = response.json()
    for i, repository in enumerate(data["items"], start=1):
        if(repository['stargazers_count']) > 10000:
            found = True
            print(f"{i}. {repository.get('name')} — ⭐ {repository.get('stargazers_count')} - {repository.get('html_url')}")
    if found:
        with open(f"{topic}_repositories.csv" , "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Repository", "Stars" , "Repository URL"])
            for repository in data["items"]:
                if (repository['stargazers_count']) > 10000:
                    writer.writerow([repository.get('name') , repository.get('stargazers_count') , repository.get('html_url')])
        print(f"CSV file created: {topic}_repositories.csv")
    else:
        print("No repositories found with more than 10,000 stars.")
else:
    print(f"API request failed: {response.status_code}")
