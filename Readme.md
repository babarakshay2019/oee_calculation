# OEE Calculation

OEE Calculation is built using Python-DRF.

## Installation Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/babarakshay2019/oee_calculation.git
    ```

2. Navigate to the project directory:

    ```bash
    cd oee_calculation
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:
    ```bash
    python manage.py runserver
    ```

#### OEE Calculation

- **Create Machine**
  - Method: POST
  - URL: `/oee/machines/`
  - Description: Create a new machine.

- **List of Machine**
  - Method: GET
  - URL: `/oee/machines/`
  - Description: List of machines.

- **Update Machine**
  - Method: PUT/PATCH
  - URL: `/oee/machines/machine_id/`
  - Description: Update machine data using id.

- **Delete Machine**
  - Method: DELETE
  - URL: `/oee/machines/machine_id/`
  - Description: Delete machine data using id.

- **Create Production Logs**
  - Method: POST
  - URL: `/oee/production_logs/`
  - Description: Create a Production Logs.

- **List of Production Logs**
  - Method: GET
  - URL: `/oee/production_logs/`
  - Description: List of created Production Logs.

- **Update Production Logs**
  - Method: PUT/PATCH
  - URL: `/oee/production_logs/machine_id/`
  - Description: Update Production Logs using id.

- **Delete Production Logs**
  - Method: DELETE
  - URL: `/oee/production_logs/machine_id/`
  - Description: Delete Production Logs using id.

- **List of OEE Calculation**
  - Method: GET
  - URL: `/oee/`
  - Description: List of OEE Calculation using machine id.

- **List of OEE Calculation Filter**
  - Method: GET
  - URL: `http://127.0.0.1:8000/oee/?machine_id=3&start_date=2024-06-21&end_date=2024-06-21`
  - Description: List of OEE Calculation apply filter using machine id and start data and end data.

  7. Run test cases:
    ```bash
    python manage.py test
    ```

8. Screen recording:
    ```bash
    https://drive.google.com/file/d/1g_rSrel0cRuOCmiDd-wAXaVUCW2_3IrI/view
    ```