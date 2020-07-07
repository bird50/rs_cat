from django.db import models

'''
[datacat]
- name (ชื่อข้อมูล)
- link  (ลิ๊งค์ของแหล่งข้อมูล)
- agency (หน่วยงานเจ้าของข้อมูล)
- agency_provided_data (หน่วยงานที่ให้ข้อมูล)
- keyword (หัวเรื่องหรือคําสําคัญ ที่ใช้สําหรับอ้างอิงในการค้นหาข้อมูล)
- description (รายละเอียดของข้อมูล)
- Time_period (ช่วงเวลาของข้อมูล)
- source (อธิบายแหล่งที่มา)
- type_of_data (รูปแบบการเก็บข้อมูล)
- date_recived  (วันที่ได้รับข้อมูล)
- reference_doc (เอกสารอ้างอิงประกอบ)
- related_subject (เรื่องที่เกี่ยวข้อง)
- access_policy (ระเบียบในการเข้าถึงข้อมูล)
- data_licensing (ระเบียบในการใช้ข้อมูล)
- tags (แท็ก)
'''
class Datacat(models.Model):
    class Type_of_data(models.TextChoices):
        CSV = 'CSV', _('CSV')
        TEXT = 'TXT', _('Text file')
        EXCEL = 'XLS', _('Excel file,xlsx,xls,xl*')
        SHP = 'SHP', _('ESRI Shape file')
        ETC = 'ETC', _('Other formats')
        UNKNOWN = 'UNK', _('Unknown format')

    ## Data licences
    ## ref https://www.cessda.eu/Training/Training-Resources/Library/Data-Management-Expert-Guide/6.-Archive-Publish/Publishing-with-CESSDA-archives/Licensing-your-data

    class Access_policy(models.TextChoices):
        CC0 = 'CC0', _('copy และ แจกจ่าย(Y) ,อางอง ผรบผดชอบเดม(N) , ใชเชงพาณชยได(Y) ,อนญาตใหปรบปรงได(Y) ,แกไขไลเซนสได(Y)')

        CC_BY = 'CC_BY', _('copy และ แจกจ่าย(Y) ,อางอง ผรบผดชอบเดม(Y) , ใชเชงพาณชยได(Y) ,อนญาตใหปรบปรงได(Y) ,แกไขไลเซนสได(Y)')


    name = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    agency = models.ForeignKey(Agency, blank=True, null=True)
    agency_provided_data = models.ForeignKey(Agency, blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    Time_period = models.TextField(blank=True)
    source = models.TextField(blank=True)
    type_of_data = models.CharField(
        max_length=3,
        choices=Type_of_data.choices,
        default=Type_of_data.UNKNOWN
    )
    date_recived = models.DateTimeField()
    reference_doc = models.TextField()
    related_subject = models.TextField()
    access_policy = models.TextField()


    created = models.DateTimeField(auto_now_add=True)

# Create your models here.
