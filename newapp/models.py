from django.db import models

COUNTRY_CHOICES = [
    ('IN', 'India'),
    ('US', 'United States'),
    ('CN', 'China'),
    ('JP', 'Japan'),
    ('DE', 'Germany'),
    ('GB', 'United Kingdom'),
    ('FR', 'France'),
    ('IT', 'Italy'),
    ('BR', 'Brazil'),
    ('CA', 'Canada'),
    ('AU', 'Australia'),
    ('RU', 'Russia'),
    ('MX', 'Mexico'),
    ('ES', 'Spain'),
    ('KR', 'South Korea'),
    ('SA', 'Saudi Arabia'),
    ('ZA', 'South Africa'),
    ('ID', 'Indonesia'),
    ('NG', 'Nigeria'),
    ('EG', 'Egypt'),
    ('AR', 'Argentina'),
    ('PK', 'Pakistan'),
    ('BD', 'Bangladesh'),
    ('TR', 'Turkey'),
    ('IR', 'Iran'),
    ('VN', 'Vietnam'),
    ('PH', 'Philippines'),
    ('TH', 'Thailand'),
    ('MY', 'Malaysia'),
    ('NL', 'Netherlands'),
    ('CH', 'Switzerland'),
    ('SE', 'Sweden'),
    ('BE', 'Belgium'),
    ('AT', 'Austria'),
    ('PL', 'Poland'),
    ('NO', 'Norway'),
    ('UA', 'Ukraine'),
    ('GR', 'Greece'),
    ('CZ', 'Czech Republic'),
    ('RO', 'Romania'),
    ('HU', 'Hungary'),
    ('PT', 'Portugal'),
    ('IE', 'Ireland'),
    ('FI', 'Finland'),
    ('DK', 'Denmark'),
    ('NZ', 'New Zealand'),
    ('CL', 'Chile'),
    ('CO', 'Colombia'),
    ('SG', 'Singapore'),
    ('HK', 'Hong Kong'),
    ('AE', 'United Arab Emirates'),
]
STATE_CHOICES = {
    'IN': [
        ('KA', 'Karnataka'),
        ('MH', 'Maharashtra'),
        ('DL', 'Delhi'),
        ('GJ', 'Gujarat'),
    ],
    'US': [
        ('CA', 'California'),
        ('TX', 'Texas')
    ],
    'CN': [
        ('BJ', 'Beijing'),
        ('SH', 'Shanghai'),
        ('GD', 'Guangdong')
    ],
    'JP': [
        ('TK', 'Tokyo'),
        ('OS', 'Osaka')
    ],
    'DE': [
        ('BE', 'Berlin'),
        ('BW', 'Baden-Württemberg'),
        ('BY', 'Bavaria')
    ],
    'GB': [
        ('ENG', 'England'),
        ('SCT', 'Scotland')
    ],
    'FR': [
        ('IDF', 'Île-de-France'),
        ('PACA', 'Provence-Alpes-Côte d\'Azur'),
        ('ARA', 'Auvergne-Rhône-Alpes')
    ],
    'IT': [
        ('LZ', 'Lazio'),
        ('LOM', 'Lombardy')
    ],
    'BR': [
        ('SP', 'São Paulo'),
        ('RJ', 'Rio de Janeiro'),
        ('MG', 'Minas Gerais')
    ],
    'CA': [
        ('ON', 'Ontario'),
        ('QC', 'Quebec')
    ],
    'AU': [
        ('NSW', 'New South Wales'),
        ('VIC', 'Victoria'),
        ('QLD', 'Queensland')
    ],
    'RU': [
        ('MOW', 'Moscow'),
        ('SPE', 'Saint Petersburg')
    ],
    'MX': [
        ('CMX', 'Mexico City'),
        ('NLE', 'Nuevo León'),
        ('JAL', 'Jalisco')
    ],
    'ES': [
        ('MD', 'Madrid'),
        ('CT', 'Catalonia')
    ],
    'KR': [
        ('11', 'Seoul'),
        ('26', 'Busan'),
        ('27', 'Daegu')
    ],
    'SA': [
        ('01', 'Riyadh'),
        ('02', 'Maka')
    ],
    'ZA': [
        ('GP', 'Gauteng'),
        ('WC', 'Western Cape'),
        ('KZN', 'KwaZulu-Natal')
    ],
    'ID': [
        ('JK', 'Jakarta'),
        ('JB', 'West Java')
    ],
    'NG': [
        ('LA', 'Lagos'),
        ('FC', 'Federal Capital Territory'),
        ('KN', 'Kano')
    ],
    'EG': [
        ('C', 'Cairo'),
        ('GZ', 'Giza')
    ],
    'AR': [
        ('B', 'Buenos Aires'),
        ('C', 'Córdoba'),
        ('S', 'Santa Fe')
    ],
    'PK': [
        ('PB', 'Punjab'),
        ('SD', 'Sindh')
    ],
    'BD': [
        ('DHK', 'Dhaka'),
        ('CTG', 'Chittagong'),
        ('RAJ', 'Rajshahi')
    ],
    'TR': [
        ('34', 'Istanbul'),
        ('06', 'Ankara')
    ],
    'IR': [
        ('THR', 'Tehran'),
        ('ISF', 'Isfahan'),
        ('KHZ', 'Khuzestan')
    ],
    'VN': [
        ('HN', 'Hanoi'),
        ('HCM', 'Ho Chi Minh City')
    ],
    'PH': [
        ('00', 'Metro Manila'),
        ('01', 'Ilocos Region'),
        ('02', 'Cagayan Valley')
    ],
    'TH': [
        ('10', 'Bangkok'),
        ('40', 'Khon Kaen')
    ],
    'MY': [
        ('10', 'Kuala Lumpur'),
        ('11', 'Putrajaya'),
        ('01', 'Johor')
    ],
    'NL': [
        ('NH', 'North Holland'),
        ('ZH', 'South Holland')
    ],
    'CH': [
        ('ZH', 'Zurich'),
        ('GE', 'Geneva'),
        ('VD', 'Vaud')
    ],
    'SE': [
        ('ST', 'Stockholm'),
        ('VG', 'Västra Götaland')
    ],
    'BE': [
        ('VAN', 'Antwerp'),
        ('OVL', 'East Flanders'),
        ('WVL', 'West Flanders')
    ],
    'AT': [
        ('WI', 'Vienna'),
        ('NOE', 'Lower Austria')
    ],
    'PL': [
        ('MZ', 'Masovian'),
        ('ML', 'Lesser Poland'),
        ('DS', 'Lower Silesia')
    ],
    'NO': [
        ('03', 'Oslo'),
        ('11', 'Rogaland')
    ],
    'UA': [
        ('30', 'Kyiv'),
        ('32', 'Kyiv Oblast'),
        ('48', 'Odessa')
    ],
    'GR': [
        ('I', 'Attica'),
        ('C', 'Central Macedonia')
    ],
    'CZ': [
        ('PR', 'Prague'),
        ('ST', 'Central Bohemia'),
        ('JM', 'South Moravia')
    ],
    'RO': [
        ('B', 'Bucharest'),
        ('CJ', 'Cluj')
    ],
    'HU': [
        ('BU', 'Budapest'),
        ('PE', 'Pest'),
        ('BA', 'Baranya')
    ],
    'PT': [
        ('LIS', 'Lisbon'),
        ('POR', 'Porto')
    ],
    'IE': [
        ('D', 'Dublin'),
        ('CW', 'Carlow'),
        ('WW', 'Wicklow')
    ],
    'FI': [
        ('18', 'Southwest Finland'),
        ('19', 'Pirkanmaa')
    ],
    'DK': [
        ('84', 'Capital Region of Denmark'),
        ('82', 'Central Denmark Region'),
        ('81', 'North Denmark Region')
    ],
    'NZ': [
        ('AUK', 'Auckland'),
        ('WGN', 'Wellington')
    ],
    'CL': [
        ('RM', 'Santiago Metropolitan'),
        ('VS', 'Valparaíso')
    ],
    'CO': [
        ('DC', 'Bogotá'),
        ('ANT', 'Antioquia'),
        ('VAS', 'Valle del Cauca')
    ],
    'SG': [
        ('01', 'Central Region'),
        ('02', 'North Region')
    ],
    'HK': [
        ('HKI', 'Hong Kong Island'),
        ('KLN', 'Kowloon')
    ],
    'AE': [
        ('AZ', 'Abu Dhabi'),
        ('DU', 'Dubai')
    ],
}
CITY_CHOICES = {
    'KA': 'Bangalore',
    'MH': 'Mumbai',
    'DL': 'New Delhi',
    'CA': 'Los Angeles',
    'TX': 'Houston',
    'BJ': 'Beijing',
    'SH': 'Shanghai',
    'GD': 'Guangzhou',
    'TK': 'Tokyo',
    'OS': 'Osaka',
    'BE': 'Berlin',
    'BW': 'Stuttgart',
    'BY': 'Munich',
    'ENG': 'London',
    'SCT': 'Edinburgh',
    'IDF': 'Paris',
    'PACA': 'Marseille',
    'ARA': 'Lyon',
    'LZ': 'Rome',
    'LOM': 'Milan',
    'SP': 'São Paulo',
}

PLANT_CATEGORIES = [
    ('flowering', 'Flowering Plants'),
    ('succulent', 'Succulents'),
    ('vegetable', 'Vegetables'),
    ('herb', 'Herbs'),
    ('fruit', 'Fruit Trees'),
    ('ornamental', 'Ornamental Plants'),
    ('cacti', 'Cacti'),
    ('indoor', 'Indoor Plants'),
    ('aquatic', 'Aquatic Plants'),
]


QUANTITY_CHOICES = [
    ('low', 'Low Quantity'),
    ('medium', 'Medium Quantity'),
    ('high', 'High Quantity'),
]
ORDER_STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('processing', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
]

BOOKING_REFERENCING_TOOL_CHOICES = [
    ('website', 'Website'),
    ('mobile_app', 'Mobile App'),
    ('phone', 'Phone'),
    ('email', 'Email'),
    ('in_person', 'In Person'),
    ('social_media', 'Social Media'),
    ('agent', 'Agent'),
]
PAYMENT_MODE = [
    ('credit_card', 'Credit Card'),
    ('debit_card', 'Debit Card'),
    ('paypal', 'PayPal'),
    ('other', 'Other'),
]

PAYMENT_STATUS = [('pending', 'Pending'),
                  ('completed', 'Completed'),
                  ('failed', 'Failed')]


# Create your models here.

class User(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)
    Date_Joined = models.DateField()


class Country(models.Model):
    Name = models.CharField(max_length=50, choices=COUNTRY_CHOICES)


class State(models.Model):
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, choices=STATE_CHOICES)


class City(models.Model):
    State = models.ForeignKey(State, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, choices=CITY_CHOICES)


class UserProfile(models.Model):  # Corrected spelling from Hodel to Model
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    BOD = models.DateField()  # Adjusted spacing
    Address = models.TextField(max_length=70)  # Fixed argument name
    Phone_No = models.BigIntegerField()  # Fixed field name to be consistent
    Image = models.ImageField(upload_to='Photos')


class PlantCategory(models.Model):
    CAT_Name = models.CharField(max_length=60, choices=PLANT_CATEGORIES)
    Description = models.TextField(max_length=70)


class Plant(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.CharField(max_length=60, choices=PLANT_CATEGORIES)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField(max_length=70)
    Stock = models.CharField(max_length=60)
    Image = models.ImageField(upload_to='Photos')


class ProductCart(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Quantity = models.CharField(max_length=60, choices=QUANTITY_CHOICES)
    Order_ID = models.CharField(max_length=50)
    Order_Status = models.CharField(max_length=60, choices=ORDER_STATUS_CHOICES)


class OrderTable(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    Quantity = models.CharField(max_length=60, choices=QUANTITY_CHOICES)
    Total_Price = models.DecimalField(max_digits=10, decimal_places=2)
    Order_Date = models.DateField()
    Delivery_Date = models.DateField()
    Status = models.CharField(max_length=60, choices=ORDER_STATUS_CHOICES, default='pending')


class PaymentTable(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Booking = models.CharField(max_length=60, choices=BOOKING_REFERENCING_TOOL_CHOICES)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Payment_Mode = models.CharField(max_length=60, choices=PAYMENT_MODE)
    Payment_Status = models.CharField(max_length=60, choices=PAYMENT_STATUS, default='pending')
    Payment_Date = models.DateField()


class Feedback(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    Rating = models.IntegerField(null=True, blank=True)
    Comment = models.TextField()
    Review_Date = models.DateField()


class Contactus(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Subject = models.CharField(max_length=70)
    Message = models.TextField()
    Phone = models.BigIntegerField()
    Created_At = models.CharField(max_length=60)
