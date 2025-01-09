# Automatic Honeygain pot draws

### Requirements

1. Linux or Mac
2. docker or systemd

### Setup

#### 1. Get JWT token

1. Login to [honeygain dashboard](https://dashboard.honeygain.com/) on web.
2. Right click and open Inspect Element / Inspect.
3. Go to "Application", "Local storage" section and find the "JWT Token".
4. Paste the token into the auth.txt file from this repository, or use it in the TOKEN env variable.

#### 2. Run App

##### 2a. With Docker

1. Get to your linux/mac system with docker installed.
2. Run this command `docker build -t hg-bot:latest . `
3. Start the docker container and run everytime on boot:
   ```docker run -d --name hg-bot -v ./auth.txt:/bot/auth.txt:ro --restart=always hg-bot:latest```
   or
   ```docker run -d --name hg-bot -e TOKEN=your-token --restart=always hg-bot:latest```


##### 2b. With systemd

1. Change user, group and path in the honeyjar.service file. 
2. `sudo cp honeyjar.service /etc/systemd/system/` 
3. `sudo systemctl daemon-reload`
4. `sudo systemctl enable --now honeyjar`
5. See logs with `sudo journalctl -u honeyjar`

# Congratulations!
