from django.contrib import admin
from .models import Restaurant, Dish, RestaurantImage, Profile, Category, DishServing, AboutContent


class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImage
    extra = 1


class DishServingInline(admin.TabularInline):
    model = DishServing
    extra = 1
    fields = ("serving_size", "price")

class DishInline(admin.TabularInline):
    model = Dish
    extra = 1
    fields = ("name", "description", "image")
    filter_horizontal = ("categories",)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "category", "open_time", "close_time", "featured")
    search_fields = ("name", "location", "category")
    list_filter = ("featured", "category")
    inlines = [RestaurantImageInline, DishInline]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "restaurant", "get_price_range", "get_categories")
    list_filter = ("restaurant", "categories")
    search_fields = ("name", "description")
    fields = ("name", "restaurant", "categories", "description", "image")
    filter_horizontal = ("categories",)
    inlines = [DishServingInline]
    
    def get_categories(self, obj):
        return ", ".join([cat.name for cat in obj.categories.all()])
    get_categories.short_description = "Categories"
    
    def get_price_range(self, obj):
        servings = obj.servings.all().order_by('price')
        if servings:
            min_price = servings.first().price
            max_price = servings.last().price
            if min_price == max_price:
                return f"₱{min_price}"
            return f"₱{min_price} - ₱{max_price}"
        return "No pricing"
    get_price_range.short_description = "Price Range"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(DishServing)
class DishServingAdmin(admin.ModelAdmin):
    list_display = ("dish", "get_serving_display", "price")
    list_filter = ("serving_size", "dish__restaurant")
    search_fields = ("dish__name",)
    
    def get_serving_display(self, obj):
        return obj.get_serving_size_display()
    get_serving_display.short_description = "Serving Size"

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "contact_number", "role", "restaurant")
    list_filter = ("role",)
    search_fields = ("user__username", "user__email", "user__first_name", "user__last_name")

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    fields = ("logo", "poster", "video")
    
    def has_add_permission(self, request):
        return not AboutContent.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False

# Register your models here.
