## Using this template repository:
- create a new repo using in [Github](https://github.com/new), selecting Repository template. Use Hearst-Hatchery/flask-slack-app-template.
- Run Cog new app command. `!new-app -t kube {name}`, this will add the proper teams, branch protection, etc. As this template just inlcudes the files in the repo.



---


## {app_name} Readme:


### {app_name}:
  - ....

## About:
  - ...


## Running locally:
  - download and install ngrok
  - start ngrok `ngrok http 80`
  - run `python app.py`
  - update [slash command](https://api.slack.com/apps/AQE4AUN9K/slash-commands) for the app to point at new ngrok tunnel.

## Testing:
  - run `bin/test`
