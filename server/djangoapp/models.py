from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name + " | " + str(self.id)
    

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=200, null=True)
    SEDAN, SUV, WAGON, TRUCK, VAN, BUSINESS = 'sedan', 'suv', 'wagon', 'truck', 'van', 'business'
    TYPES = [SEDAN, SUV, WAGON, TRUCK, VAN, BUSINESS]
    type = models.CharField(choices=[(x, x) for x in TYPES], max_length=10)
    year = models.DateField(null=True)
    def __str__(self):
        return f"{self.car_make} {self.type} {self.year}"
    


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Full name of the dealer
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.id = id
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        def __str__(self):
            return (f"Dealer Review: \n"
                    f"Name: {self.name}\n"
                    f"Dealership: {self.dealership}\n"
                    f"Review: {self.review}\n"
                    f"Purchase: {self.purchase}\n"
                    f"Purchase Date: {self.purchase_date}\n"
                    f"Car Make: {self.car_make}\n"
                    f"Car Model: {self.car_model}\n"
                    f"Car Year: {self.car_year}\n"
                    f"Sentiment: {self.sentiment}")
        