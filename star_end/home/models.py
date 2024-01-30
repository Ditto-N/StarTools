from django.db import models

class Tool(models.Model):
  title = models.CharField(unique=True, max_length=10, verbose_name="tool name")
  description = models.CharField(max_length=100, verbose_name="tool description")

  class Meta:
    verbose_name = verbose_name_plural = "tools"
    db_table = "tools_info"