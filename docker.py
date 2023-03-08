import os

HOSTNAME = "gcr.io"
PROJECT_ID = "bonion"
TARG_IMG = "test-app"
TAG = "latest"


def build_container():
  os.system("""
    docker build -t {}/{}/{}:{} .
  """.format(HOSTNAME, PROJECT_ID, TARG_IMG, TAG))

def run_local_container():
  os.system("""
    docker run --publish 8000:8000 gcr.io/bonion/test-app
  """)

def push_container():
  os.system("""
    docker push {}/{}/{}:{}
  """.format(HOSTNAME, PROJECT_ID, TARG_IMG, TAG))

if __name__=="__main__":
  build_container()
  # run_local_container()
  push_container()