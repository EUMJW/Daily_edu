from django.db import models

# Create your models here.
# 클래스를 정의한다.
# 이 클래스를 가지고 테이블을 관리한다.

class TestClass(models.Model):
    # 자동으로 1씩 증가하는 컬럼
    test_idx = models.AutoField(primary_key=True)
    # 문자열 컬럼
    test_str = models.TextField(null=False)
    # 정수 컬럼
    test_int = models.IntegerField(null=False)
