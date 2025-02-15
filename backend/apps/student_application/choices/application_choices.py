from django.db import models


class StatusChoices(models.TextChoices):
    IN_WORK = "In work"
    DUBBING = "Dubbing"
    NEW = "New"
    AGREE ="Agree"
    DISAGREE ="Disagree"
    
class CoursesChoices(models.TextChoices):
    FS = "FS"
    QACX = "QACX"
    JCX = "JCX"
    JSCX = "JSCX"
    FE = "FE"
    PCX = "PCX"

class TypeCourseChoices(models.TextChoices):
    PRO = "pro"
    MINIMAL = "minimal"
    PREMIUM = "premium"
    INCUBATOR = "incubator"
    VIP = "vip"

class FormatCourseChoices(models.TextChoices):
    STATIC = "static"
    ONLINE = "online"

