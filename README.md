# B-Onion-TopicDemo

## Instructions to Follow Demo

### Google Container Registry
1. Find hostname for repo, should be gcr.io given our location.

1. Choose target image name, this can be different to an images local name

1. Combine into format *Hostname*/*Project_ID*/*target_img* you will use this when tagging your local image using the format 

~~~
docker build -t HOSTNAME/PROJECT-ID/TARGET-IMAGE:TAG .
~~~

<!-- - **SOURCE_IMAGE** is the local image name or image ID -->
- **HOSTNAME** is the registry host you chose in step 2.
- **PROJECT** is the Google Cloud project ID.
- **TARGET-IMAGE** is the name for the image when it's stored in Container Registry.
- **TAG** is the tag you want to associate with this image version.

4. Ensure that you have authentication to push your container and a repository to push to. 

1. If you haven't downloaded gcloud and authenticated use:
  - [Install GCloud CLI](https://cloud.google.com/sdk/docs/install)
  - [link to authenticate docker](https://cloud.google.com/container-registry/docs/advanced-authentication#linux)

5. Push the tagged image using 
~~~
docker push HOSTNAME/PROJECT-ID/IMAGE:TAG
~~~

### Getting Cloud Run set up
1. go to google cloud console cloud run

2. Create a service, make sure to 
  - select the image url you just pushed
  - set the port to the port which you defined in the app (8000)

