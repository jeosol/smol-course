# Main course repository: https://github.com/huggingface/smol-course/tree/main
NAME=smol-course
PYVERSION=3.12

# Notebook tips:
# To convert a code cell to text cell: Ctrl + M, then M
# To covert a text cell to code cell: Ctrl + M, then Y

# Adjust size of headers:
# use # (Heading 1, Largest), 
# use ## heading 2
# use ### Heading 3
# or for precise size control use:
# <font size="5"> Your Text </font>
#app-version:
#	echo "COMMIT_ID=${COMMIT_ID}"

venv:
	uv venv /tmp/venv/${NAME} --python ${PYVERSION}

source-env:
	echo source /tmp/venv/${NAME}/bin/activate

deactivate:
	deactivate

install:
	uv pip install -r requirements.txt

build-docker-image:
	export DOCKER_BUILDKIT=1 && \
	docker image build \
	-t ${NAME}:${COMMIT_ID} . 

run:
	python src/main.py
