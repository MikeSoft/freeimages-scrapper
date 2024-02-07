from celery import shared_task
from celery.utils.log import get_logger
from .freeimages_service import FreeImagesService
from ..models import Search, Image, Tag, ImageTag

logger = get_logger(__name__)

freeimage_service = FreeImagesService()


@shared_task(ignore_result=True)
def command(search_text: str = None, max_results: int = 100):
    logger.info(f"get_photos_service started {search_text} {max_results}")
    images = freeimage_service.get_images(search_text, max_results=max_results)
    logger.info(f"get_photos_service images {images}")
    text_tags = set([tag for img in images for tag in img["tags"]])

    tags = {text: Tag.objects.get_or_create(name=text)[0] for text in text_tags}
    logger.info(f"get_photos_service text_tags {tags}")
    for img in images:
        image, created = Image.objects.get_or_create(title=img["title"], url=img["url"])
        for tag in img["tags"]:
            ImageTag.objects.get_or_create(image=image, tag=tags[tag])
