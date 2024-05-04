from django.db import models


class ReadHistory(models.Model):
    name = models.CharField(
        "名前",
        max_length=255,
        choices=(
            ("altnight", "あるとな"),
            ("furi", "ふり"),
        )
    )
    category = models.CharField(
        "カテゴリ",
        max_length=255,
        choices=(
            ("tech", "技術書"),
            ("business", "ビジネス書"),
        )
    )
    title = models.CharField(
        "書籍名",
        max_length=255
    )
    price = models.IntegerField("価格")
    read_at = models.DateField("読了日")
    is_public = models.BooleanField("公開するかどうか")
    is_favorite = models.BooleanField(
        "評価",
        blank=True,
        null=True
    )

    class Meta:
        db_table = "read_history"
