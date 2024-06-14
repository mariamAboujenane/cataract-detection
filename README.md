# Smart Cataract Detection

This Flask web application uses the Roboflow API to perform smart cataract detection on uploaded images. The application allows users to upload an image, processes it using a pre-trained model, and returns the classification result with confidence levels.

## Features

- Upload images via a web interface.
- Process images with a pre-trained model from Roboflow.
- Display classification results with confidence levels.
- User-friendly interface with drag-and-drop image upload functionality.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/smart-cataract-detection.git
    cd smart-cataract-detection
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Set up your Roboflow API key and model ID. Replace `your_api_key` and `your_model_id` with your actual Roboflow API key and model ID in the `app.py` file:
    ```python
    CLIENT = InferenceHTTPClient(
        api_url="https://classify.roboflow.com",
        api_key="your_api_key"
    )
    ```

## Running the Application

1. Start the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

## Project Structure
- `static/images/`: Contains static images used in the application.
- `templates/`: Contains HTML templates for the application.
- `uploads/`: Directory for storing uploaded images temporarily.
- `app.py`: The main Flask application file.
- `requirements.txt`: Contains the list of dependencies.

## Usage

1. Go to the home page.
![image](https://github.com/mariamAboujenane/cataract-detection/assets/106840796/12605eeb-8d9c-45d3-9945-60327c413d77)
2. Upload an image by clicking the "Select an image" button or by dragging and dropping an image.
![image](https://github.com/mariamAboujenane/cataract-detection/assets/106840796/ed8e2063-3b4f-4abe-869f-b717d3b27603)
3. View the classification result and confidence score on the result page.
![image](https://github.com/mariamAboujenane/cataract-detection/assets/106840796/5f3bac21-8485-447e-a3a1-a1a14e2167cb)
![image](https://github.com/mariamAboujenane/cataract-detection/assets/106840796/b82f502d-adf2-42d4-b2a9-650ea418a581)

## Dependencies

- Flask
- Werkzeug
- inference-sdk

