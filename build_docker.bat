docker build -t dactyl-keyboard -f docker/Dockerfile .
docker run --name DM-Build-Single -d -v "%cd%/:/app"  dactyl-keyboard python3 -i dactyl_manuform.py
docker run --name DM-Config -d -v "%cd%/:/app"  dactyl-keyboard python3 -i generate_configuration.py
docker run --name DM-Build-All -d -v "%cd%/:/app"  dactyl-keyboard python3 -i model_builder.py
docker run --name DM-Shell -d -ti -v "%cd%/:/app"  dactyl-keyboard
