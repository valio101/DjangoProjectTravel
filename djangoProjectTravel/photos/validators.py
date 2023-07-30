from django.core.exceptions import ValidationError


def validate_image_less_than_5mb(image):
    filesize = image.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))