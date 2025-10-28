# 📦 File Upload Service

A simple service for uploading and downloading files using curl.
Infrastructure is provisioned with Terraform, and the service runs in a Docker container.

## 🚀 Getting Started
1. Initialize and Apply Terraform

# Start
```
cd terraform
terraform init
terraform apply -auto-approve
```
## 📤 Upload a File
```
curl -F 'file=@/path/file.txt' http://localhost:5050/upload
```

✅ Response Example:
```
File uploaded successfully with link /files/xxxx-xxxx-xxxx
```

## 💾 Download a File

```
curl http://localhost:5050/files/<file.txt> --ouput <file.txt>
```
Using the ID:
```
curl http://localhost:5050/files/xxxx-xxxx-xxxx --ouput <file.txt>
```
## 🛑 Stop the Running Container
```
docker ps

docker stop <CONTAINER ID>
```
