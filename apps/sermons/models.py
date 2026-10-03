from django.db import models
from django.urls import reverse
from urllib.parse import urlparse, parse_qs

class Sermon(models.Model):

    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True
    )

    speaker = models.CharField(
        max_length=200
    )

    sermon_date = models.DateField()

    scripture = models.CharField(
        max_length=255,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    audio_url = models.URLField(
        blank=True,
        help_text="Link to the sermon audio."
    )

    video_url = models.URLField(
        blank=True,
        help_text="YouTube, Vimeo, or other video link."
    )

    thumbnail = models.ImageField(
        upload_to="sermons/",
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=100,
        blank=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
    youtube_url = models.URLField(
        blank=True,
        help_text="Paste the YouTube URL for this sermon."
    )

    class Meta:
        ordering = ["-sermon_date", "-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "sermons:detail",
            kwargs={"slug": self.slug}
        )
@property
def youtube_video_id(self):

    if not self.youtube_url:
        return ""

    url = self.youtube_url.strip()

    parsed = urlparse(url)

    # Standard URL:
    # https://www.youtube.com/watch?v=VIDEO_ID

    if parsed.hostname in ("www.youtube.com", "youtube.com"):
        video_id = parse_qs(parsed.query).get("v")

        if video_id:
            return video_id[0]

        # Also support:
        # https://www.youtube.com/embed/VIDEO_ID

        if parsed.path.startswith("/embed/"):
            return parsed.path.split("/embed/")[1].split("/")[0]

        # Also support:
        # https://www.youtube.com/shorts/VIDEO_ID

        if parsed.path.startswith("/shorts/"):
            return parsed.path.split("/shorts/")[1].split("/")[0]

    # Support:
    # https://youtu.be/VIDEO_ID

    if parsed.hostname == "youtu.be":
        return parsed.path.strip("/").split("/")[0]

    return ""
