from django.contrib import admin

# Register your models here.
from .models import *

class UserAdmin(admin.ModelAdmin):
	list_display = ['username','nama_user','role']
	search_fields = ['username','nama_user','role']
	class Meta:
		model = User

class JadwalKelasAdmin(admin.ModelAdmin):
	list_display = ['dosen','hari','jam_mulai','jam_selesai','ruangan']
	search_fields = ['dosen','hari','jam_mulai','jam_selesai','ruangan']
	class Meta:
		model = JadwalKelas

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ['nama_restoran']
	search_fields =['nama_restoran']
	class Meta:
		model = Restaurant
		
class FoodAdmin(admin.ModelAdmin):
	list_display = ['restoran','nama_makanan','total_rating']
	search_fields = ['restoran','nama_makanan','total_rating'] 
	class Meta:
		model = Food

class OrderAdmin(admin.ModelAdmin):
	list_display = ['waktu_order','dosen']
	search_fields = ['waktu_order','dosen']
	class Meta:
		model = Order

class OrderItemAdmin(admin.ModelAdmin):
	list_display = ['order','food','kuantitas','tipe_konsumen','permintaan_lain']
	search_fields = ['order','food','kuantitas','tipe_konsumen','permintaan_lain']
	class Meta:
		model = OrderItem

class ReviewAdmin(admin.ModelAdmin):
	list_display = ['food','rating','komentar','dosen']
	search_fields = ['food','rating','komentar','dosen']
	class Meta:
		model = Review

class PembayaranAdmin(admin.ModelAdmin):
	list_display = ['waktu_bayar','sekretariat']
	search_fields = ['waktu_bayar','sekretariat']
	class Meta:
		model = Pembayaran		
		
admin.site.register(User, UserAdmin)
admin.site.register(JadwalKelas, JadwalKelasAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Pembayaran, PembayaranAdmin)
