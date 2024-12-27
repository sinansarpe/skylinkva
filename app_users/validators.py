from django.core.exceptions import ValidationError
from PIL import Image

def validate_screenshot(image):
    """
    Validates the uploaded image for extension (PNG or JPG) and aspect ratio (16:9).

    Raises ValidationError if the image is invalid.
    """
    allowed_extensions = ['png', 'jpg', 'jpeg']
    extension = image.name.split('.')[-1].lower()
    if extension not in allowed_extensions:
        raise ValidationError(f'Invalid image format. Only PNG or JPG images are allowed.')

    try:
        with Image.open(image) as img:
            width, height = img.size
            if width / height != 16 / 9:
                raise ValidationError('Image must be in 16:9 aspect ratio.')
    except OSError:
        raise ValidationError('Unable to open the uploaded image.')