import bs4 as bs
import requests
from celery.utils.log import get_logger

logger = get_logger(__name__)


class FreeImagesService:
    def __init__(self):
        self.base_url = "https://www.freeimages.com/search/{query}/{page}"
        self.base_div = "grid-container"
        self.avoid_image_list = ["https://static.freeimages.com/assets/icons/istock_logo.svg", ]
        self.tags_tag = "tags-container"

    def search(self, query, page, ):
        url = self.base_url.format(query=query, page=page)
        response = requests.get(url)
        soup = bs.BeautifulSoup(response.text, "html.parser")
        div = soup.find("div", {"class": self.base_div})

        images = []
        for article in div.find_all("article"):
            img = article.find("img")
            src = img.get("src")
            if not src.startswith("data:image") and src not in self.avoid_image_list:
                src = src.split("?")[0]
                tags = [tag.text.strip() for tag in article.find("div", {"class": "tags-container"}).find_all("a")]
                data = {
                    "title": img.get("alt"),
                    "url": src,
                    "tags": tags
                }
                images.append(data)

        return images

    def get_images(self, query, max_results, max_pages=20):
        logger.info(f"get_images(query={query}, max_results={max_results})")
        images = []
        for page in range(1, max_pages):
            logger.info(f"search(query={query}, page={page})")
            images += self.search(query, page)
            if len(images) >= max_results:
                logger.info(f"get_images BREAK len={len(images)} >= {max_results}")
                break
        return images
