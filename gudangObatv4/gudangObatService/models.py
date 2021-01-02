from django.db import models

class Drugs (models.Model):
	kodeObat = models.CharField(max_length = 10, primary_key=True)
	namaOBat = models.CharField(max_length=20)

	def __str__(self):
		return self.kodeObat

class Puskesmas (models.Model):
	kodePkm = models.CharField(max_length = 10, primary_key=True)
	namaPkm = models.CharField(max_length=20)
	alamat = models.CharField(max_length=20)

	def __str__(self):
		return self.kodePkm

class DrugsQuantity (models.Model):
	kodeObat = models.ForeignKey(Drugs, on_delete=models.CASCADE)
	kodePkm = models.ForeignKey(Puskesmas, on_delete=models.CASCADE)
	jumlah = models.PositiveIntegerField()
	tanggal = models.DateField()

	def __str__(self):
		return str(self.kodeObat)