document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('car-list')) {
        fetch('/api/cars')
            .then(response => response.json())
            .then(data => {
                const carList = document.getElementById('car-list');
                carList.innerHTML = ''; // Clear existing content
                data.forEach(car => {
                    const carItem = document.createElement('div');
                    carItem.className = 'car';
                    carItem.innerHTML = `
                        <img src="/static/images/${car.image}" alt="${car.make} ${car.model}">
                        <h3>${car.make} ${car.model} (${car.year})</h3>
                        <p>${car.description}</p>
                        <button class="btn">Rent Now</button>
                    `;
                    carList.appendChild(carItem);
                });
            })
            .catch(error => console.error('Error fetching cars:', error));
    }
});