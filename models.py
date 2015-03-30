from django.db import models

class User(models.Model):
	username = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=20)
	role = models.CharField(max_length=15)
	nama_user = models.CharField(max_length=45)
	
class Jadwal_kelas(models.Model):
	dosen = models.ForeignKey(User)
	hari = models.CharField(max_length=20)
	jammulai = models.TimeField(max_length=15)
	jamselesai = models.TimeField(max_length=45) 
	ruangan = models.CharField(max_length=5)

class Order(models.Model):
	waktu_order = models.DateTimeField(max_length=20) 
	dosen = models.ForeignKey(User)
	sekretariat = models.ForeignKey(User)

class Order_item(models.Model):
	order = models.ForeignKey(Order)
	food = models.ForeignKey(Food)
	qty = models.IntegerField(default=0)
	consumer_type = models.CharField(max_length=10)

class Food(models.Model):
	nama = models.CharField(max_length=30)
	total_rating = models.IntegerField(default=0)

class Review(models.Model):
	food = models.ForeignKey(Food)
	rating = models.IntegerField(default=0) 
	komentar = models.CharField(max_length=50)
	dosen = models.ForeignKey(User)

class Pembayaran(models.Model):
	waktu_bayar = models.DateTimeField(max_length=10)
	total_pembayaran = models.IntegerField(default=0)
	sekretariat = models.ForeignKey(User) 



	
	
