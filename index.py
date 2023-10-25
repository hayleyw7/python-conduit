import subprocess

command = """
  curl -X POST https://app.leadconduit.com/flows/64f88c209fdcbc91ead79a18/sources/64f88bb312e29022f8da4df2/submit \
  -H "Accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "first_name=Hayley" \
  --data-urlencode "last_name=Witherell" \
  --data-urlencode "email=hayleywitherell@gmail.com" \
  --data-urlencode "repo_url=https://github.com/hayleyw7/hayleyw7"
"""

subprocess.run(command, shell=True, check=True, text=True)
