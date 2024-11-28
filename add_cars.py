from run import create_app, db
from app.car import Car

app = create_app()

with app.app_context():
    # Example car data
    cars = [
    Car(
        brand="Toyota",
        make="Toyota",
        model="Corolla",
        year=2020,
        price=20000,
        availability=True,
        description="A reliable sedan with excellent fuel efficiency and advanced safety features.",
        image="car_1.png"
    ),
    Car(
        brand="Honda",
        make="Honda",
        model="Civic",
        year=2019,
        price=19000,
        availability=True,
        description="A compact car known for its smooth ride and modern technology.",
        image="car_2.png"
    ),
    Car(
        brand="Ford",
        make="Ford",
        model="Focus",
        year=2021,
        price=22000,
        availability=False,
        description="A sporty hatchback with great handling and a sleek design.",
        image="car_3.png"
    ),
    Car(
        brand="Chevrolet",
        make="Chevrolet",
        model="Malibu",
        year=2018,
        price=18000,
        availability=True,
        description="A midsize sedan offering a comfortable interior and efficient performance.",
        image="car_4.png"
    ),
    Car(
        brand="Tesla",
        make="Tesla",
        model="Model 3",
        year=2022,
        price=45000,
        availability=False,
        description="A fully electric sedan with cutting-edge technology and impressive range.",
        image="car_5.png"
    ),
    Car(
        brand="BMW",
        make="BMW",
        model="3 Series",
        year=2021,
        price=41000,
        availability=True,
        description="A luxury sedan offering a powerful engine and premium features.",
        image="car_6.png"
    ),
    Car(
        brand="Mercedes-Benz",
        make="Mercedes-Benz",
        model="C-Class",
        year=2020,
        price=43000,
        availability=False,
        description="A high-end sedan with sophisticated design and superior comfort.",
        image="car_7.png"
    ),
    Car(
        brand="Hyundai",
        make="Hyundai",
        model="Elantra",
        year=2019,
        price=17000,
        availability=True,
        description="A budget-friendly car with a stylish exterior and modern amenities.",
        image="car_8.png"
    ),
    Car(
        brand="Nissan",
        make="Nissan",
        model="Altima",
        year=2021,
        price=21000,
        availability=True,
        description="A reliable midsize sedan with excellent safety ratings and a smooth ride.",
        image="car_9.png"
    ),
    Car(
        brand="Volkswagen",
        make="Volkswagen",
        model="Passat",
        year=2017,
        price=16000,
        availability=False,
        description="A spacious sedan with a refined interior and strong performance.",
        image="car_10.png"
    )
    ]
    db.session.bulk_save_objects(cars)
    db.session.commit()

    print("Cars added!")
