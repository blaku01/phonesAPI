import csv
from phone.models import Phone
from phone.serializers import PhoneDetailSerializer
from phone.utils import get_image
with open("phones_data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[-1] == "release_date":
            continue
        date_MM = row[12][:2]
        if date_MM[-1] == "-":
            date_MM = date_MM[0]
        date_YYYY = row[12][-4:]
        phone = Phone(
            brand_name = row[1],
            model_name = row[2],
            os = row[3],
            popularity = int(float(row[4])),
            best_price = int(float(row[5])),
            lowest_price = int(float(row[6])),
            highest_price = int(float(row[7])),
            sellers_amount = int(float(row[8])),
            screen_size = int(float(row[9])),
            memory_size = int(float(row[10])),
            battery_size = int(float(row[11])),
            release_date = date_YYYY + "-" + date_MM + "-01",
            )
        serialized_phone = PhoneDetailSerializer(phone)
        phone_data = serialized_phone.data
        del phone_data['image_url']
        serialized_phone.create(validated_data=phone_data)
        # creates a tuple of the new object or
        # current object and a boolean of if it was created
