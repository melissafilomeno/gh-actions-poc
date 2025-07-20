import argparse
import sys
import requests

def get_posts(github_token):
  url = "https://api.github.com/repos/melissafilomeno/gh-actions-3-poc/actions/artifacts"

  try:
    headers = {
      "Accept" : "application/vnd.github+json",
      "Authorization" : "Bearer {}".format(github_token),
      "X-GitHub-Api-Version" : "2022-11-28"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
      posts = response.json()
      return posts
    else:
      print("Error:", response.status_code)
      return None

  except requests.exceptions.RequestException as e:
    print('Error:', e)
    return None

def main() -> int:
  parser = argparse.ArgumentParser()
  parser.add_argument('--input1')
  parser.add_argument('--github_token')
  args = parser.parse_args()

  contents = get_posts(args.github_token)
	
  print("input1 = {}".format(args.input1))
  print("github_token length = {}".format(len(args.github_token)))
  print("gh-actions-3-poc contents = {}".format(contents))
  print("""

	line1
	line2
	
	line3
	line4

  """)
  return 0

if __name__ == '__main__':
  sys.exit(main())
