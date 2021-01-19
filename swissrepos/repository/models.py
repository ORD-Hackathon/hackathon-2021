from django.db import models

class MaturityLevel(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


class Metric(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


class Repository(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    disciplines = models.CharField(max_length=5000, null=True)
    content_types = models.CharField(max_length=5000, null=True)
    maturity_level = models.ForeignKey(MaturityLevel, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Repositories"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Indicator(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


class IndicatorValue(models.Model):
    maturity_level = models.ForeignKey(MaturityLevel, on_delete=models.CASCADE)
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)


class MetricCategory(models.Model):
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    maturity_level = models.ForeignKey(MaturityLevel, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "MetricsCategories"


class IndicatorCategory(models.Model):
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weight = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "IndicatorsCategories"