# Resource Pack Server
This is a small Python http server to help host your resource packs for a Minecraft server.
## Why was this even here?
This software is created to assist issue with Oraxen's Polymath server.
It is created a a simple replacement of Polymath, that indirectly interact with the server.
But it can also host some of your resource packs as well.
This creates an HTTP server that your Minecraft server needs to link to, hosting the file for the players to download without actually using Polymath.
I keep having errors, then I figured I don't need Polymath, just some HTTP server that hosts my pack. 
## Installation
1. Download the Python script in the Releases section and place it within the same directory as the Resource Pack.
2. Install Python
3. Run the server by with ```python pack-host.py```
4. As this script is designed with the enviornment of [Oraxen](https://oraxen.com). It looks and hosts the pack.zip by default. So just drop it in the Oraxen/pack folder
5. Add a few configuration to the server.properties, as Oraxen does not directly support this server.
```
resource-pack=(Public IP):(Port)/pack.zip
```
6. Join and test the resource pack server!
## Configuration
To configure this script, just open it up in any text editor of your choice.
You will see some variables , ```PORT``` and ```FILE_NAME```
The ```PORT``` variable controls which port the server will run on.
The ```FILE_NAME``` variable is the only file that can be accessed through this server. Configured through a name, and probably with a zip as well.
## Notes
There are a few vulnerabilities that you need to be careful of.
1. The pack.zip file is globally accessible, so make sure no other files in the subdirectories are named pack.zip
2. There are no protection, so if you wanted to use this for production, I recommend stress-testing it first and fix all issues.
## License
This project is licensed under MediumCraft Protective License 1.0.
Permissions:
* Distribute binaries and source code
* Modify and use my work publically
