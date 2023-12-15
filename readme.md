# Drone Plugin for Upload S3

A Drone plugin for uploading your generated file to S3 Bucket

## How to Use

On your .drone.yml add step with this plugin. Also you can use drone secret to import settings to the plugin.

```yml
steps:
  # ...
  - name: upload s3
    image: ilhamfadhilah/drone-s3-uploader:v1.0.0
    settings:
      endpoint:
        from_secret: endpoint
      access_key:
        from_secret: access_key
      secret_key:
        from_secret: secret_key
      bucket:
        from_secret: bucket
      target:
      source:
  # ...
```
