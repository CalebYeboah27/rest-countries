# API Data Fetching and Storage to Excel

This repository contains a Python script that demonstrates how to fetch data from APIs using the `requests` library and store the retrieved data in an Excel file using the `pandas` library. This can be particularly useful when you need to collect data from different APIs and consolidate them into a single Excel file for analysis or reporting purposes.

## Getting Started

### Prerequisites

To run the script successfully, you'll need to have the following:

- Python (>= 3.6)
- `requests` library (install using `pip install requests`)
- `pandas` library (install using `pip install pandas`)

### Installation

1. Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/your-username/api-data-to-excel.git
   ```

2. Navigate to the project directory:

   ```bash
   cd api-data-to-excel
   ```

3. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open the `config.json` file and update it with the API endpoints you want to fetch data from. You can also customize other parameters like request headers, query parameters, etc.

2. Run the Python script:

   ```bash
   python fetch_and_store.py
   ```

   The script will fetch data from the specified APIs and store the data in an Excel file named `output_data.xlsx`.

## Configuration

- In the `.env` file, you can store your API_BEARER_TOKEN that would be provided by the TMDB api:
- `"endpoints"`: List of API endpoints to fetch data from.
- `"headers"` (optional): Request headers to include while making API requests.
- `"params"` (optional): Query parameters to pass in the API requests.
- `"output_file"`: Name of the Excel file to store the fetched data.

## Customization

You can customize the script further based on your needs:

- Modify the data parsing logic in the `fetch_and_store_data()` function to extract relevant information from the API response.
- Adjust the Excel file format or data storage method by modifying the `store_to_excel()` function.
- Implement error handling and logging mechanisms for better reliability.

## Contributing

Contributions are welcome! If you have any improvements or feature suggestions, please feel free to submit a pull request.

## License

This project is licensed under the MIT License. You can find the details in the [LICENSE](LICENSE) file.

---

Happy data fetching and Excel storing! If you have any questions or issues, please don't hesitate to open an issue in this repository.
