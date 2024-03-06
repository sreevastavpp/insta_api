```yaml
openapi: 3.0.0
info:
  title: Image Upload API
  version: '1.0'
paths:
  /upload:
    post:
      summary: Uploads an image
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
      responses:
        '200':
          description: OK
        '400':
          description: Bad request
```

```python
import os
import connexion

# Create a Flask app instance
app = connexion.FlaskApp(__name__, specification_dir='./')
app.add_api('swagger.yaml')

# Create an upload directory if it doesn't exist
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Define the upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    file = connexion.request.files['file']
    if file:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)
        return 'File uploaded successfully'
    else:
        return 'No file selected'

# Start the Flask app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
```