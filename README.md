# Start
```
cd terraform
terraform init
terraform apply -auto-approve
```
# Upload file

curl -F 'file=@/path/file.txt' http://localhost:5050/upload


# To download file

> File uploaded successfully with link /files/xxxx-xxxx-xxxx
```
curl http://localhost:5050/files/<file.txt> --ouput <file.txt>
```
OR
```
curl http://localhost:5050/files/xxxx-xxxx-xxxx --ouput <file.txt>
```
#To stop container
```
docker ps

docker stop <CONTAINER ID>
```
