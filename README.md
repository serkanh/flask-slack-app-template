## Using this template repository:
- create a new repo using in [Github](https://github.com/new), selecting Repository template. Use Hearst-Hatchery/flask-slack-app-template.
- Run Cog new app command. `!new-app -t kube {name}`, this will add the proper teams, branch protection, etc. As this template just inlcudes the files in the repo.

- Since there are a few files already you'll need to change both the [k8s/deployment.yml](k8s/deployment.yml) and [k8s/service.yml](k8s/service.yml), replacing all instances of `flask-slack-app-template` with your app name. As new-app, skips pre-exisiting files.


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

## Running locally on Docker:
  - download and install ngrok
  - run `docker-compose up -d`
  - run `docker ps` and get the port that Docker is mapping the container to, i.e. `0.0.0.0:32769->80/tcp`
  - run `ngrok http 32769` (the port from the above step)

## Testing:
  - run `bin/test`
