from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import setting

class GoogleCloudStaticFileStorage(GoogleCloudStorage):
    """
    Google file storage class which gives a media file path from MEDIA_URL not google generated one.
    """
    
    bucket_name = setting('GS_STATIC_BUCKET_NAME')