docker build -t dactyl-keyboard -f docker/Dockerfile .
docker run --name WB-Build-Single -d -v "%cd%/src:/app/src" -v "%cd%/things:/app/things" -v "%cd%/things:/app/configs"  dactyl-keyboard python3 -i dactyl_manuform.py
docker run --name WB-Config -d -v "%cd%/src:/app/src" -v "%cd%/things:/app/things" -v "%cd%/things:/app/configs" dactyl-keyboard python3 -i generate_configuration.py
docker run --name WB-Build-All -d -v "%cd%/src:/app/src" -v "%cd%/things:/app/things" -v "%cd%/things:/app/configs" dactyl-keyboard python3 -i model_builder.py
docker run --name WB-Shell -d -ti -v "%cd%/src:/app/src" -v "%cd%/things:/app/things"  -v "%cd%/things:/app/configs" dactyl-keyboard
