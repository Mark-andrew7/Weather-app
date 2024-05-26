# Weather_Wise :hammer:

## Overview

The Weather App is a web application that allows users to search for the current weather conditions and a 5-day weather forecast for any city. This project demonstrates the use of Django for the backend, React for the frontend, and Tailwind CSS for styling.

## Features

- Search for current weather conditions by city name
- View detailed 5-day weather forecast
- Responsive design that works on both desktop and mobile devices
- Error handling and user-friendly notifications

## Tech Stack

- **Frontend:** React, Tailwind CSS
- **Backend:** Django, Django REST Framework
- **APIs:** OpenWeatherMap API for weather data, Geocoding API for converting city names to coordinates

## Setup Instructions

### Prerequisites

- Python 3.x
- Node.js and npm
- Django
- Create React App

### Backend Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Mark-andrew7/Weather-app
    cd weather-app
    ```

2. **Set up the Django environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Create a `.env` file in the project root and add your OpenWeatherMap API key:**

    ```env
    OPENWEATHERMAP_API_KEY=your_api_key_here
    ```

4. **Run migrations and start the Django server:**

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

### Frontend Setup

1. **Navigate to the frontend directory and install dependencies:**

    ```bash
    cd weather-frontend
    npm install
    ```

2. **Set up Tailwind CSS:**

    - Ensure `tailwind.config.js` is configured properly.
    - Include Tailwind in your CSS by adding the following lines to `src/index.css`:

    ```css
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```

3. **Build and start the React app:**

    ```bash
    npm start
    ```

## Project Structure




## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Caleb Baraka - [@your_twitter_handle](https://x.com/Calebbarak81904) - calebbaraka79@gmail.com
>>>>>>> 705e2839e96f9632d3a4025bc8065048ad730f0d
