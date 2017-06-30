import os
from datetime import datetime
from rest_uploads.settings import BASE_DIR
from uploads.models import Upload

# Create your tasks here

def delete_old_posts():
    data = Upload.objects.all()
    for item in data:
        if (datetime.now().date() - item.uploaded.date()).days > 7:
            file = BASE_DIR + '/rest_uploads/media/' + item.file.name
            item.delete()
            os.remove(file)
