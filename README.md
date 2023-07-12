# Tactico
## Football scouting recommender system using machine learning
This project is a machine recommender system using machine learning specifically **Dimensionality Reduction** using **PCA**.   
It is purely based on statistics and ignores all other factors.

The data used is from [FBref](https://fbref.com/en/).  
The data is extracted using web scraping and then converted to per90 to level the playing field. Code for this is in the data_scraping folder.  

The generate_data folder contains the code for generating the pickle files. This won't be needed to run the application as the data has already been preprocessed.

## Installation 
To set up and run the Football Recommender System, follow these steps:

### Prerequisites
- Python 3.x
- pip package manager

### Backend Setup

1. Clone the repository:

```bash
git clone https://github.com/KasuniB/Tactico
```
2. Navigate to the project directory  
3. Install the required Python packages:
```bash
pip install pandas  
pip install flask
pip install pickle
```
## Usage
Follow these steps to use the Football Recommender System:  

1. Start the Flask API by running the following command:
```bash
python app.py
```
The API will start running on http://localhost:5000.

2. Access the API endpoints to make recommendations. The available endpoints are:  
/recommend: Accepts a JSON payload with user input and returns player recommendations based on the provided parameters.
Example JSON payload:
```bash
{
  "player_type": "Outfield players",
  "query": "Lionel Messi(PSG)",
  "count": 5,
  "comparison": "All positions",
  "league": "La Liga"
}
```
The API can be tested using Postman or any application you might be comfortable with

## Credits
The development of this project was made possible by the following individuals:

[Moses Kasuni](https://github.com/KasuniB) 
[Eric Mutunga](https://github.com/Eric-MK)  
We also extend our gratitude to the developers of Python 

## Contributing
Contributions to the Football Recommender System are welcome! If you have any ideas, improvements, or bug fixes, please open an issue or submit a pull request.
