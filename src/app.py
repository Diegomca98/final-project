from flask import Flask, render_template

app = Flask(__name__)

app.route('/')
def index():
    return render_template('index.html')

app.route('/dataset-information')
def about_dataset():
    columns = [
        {'name': 'FlightDate', 'description':'Flight Date (yyyymmdd)', 'type': 'Datetime'}, 
        {'name': 'Airline', 'description': 'Airline Name', 'type': 'String'}, 
        {'name': 'Cancelled', 'description': 'Cancelled Flight Indicator (1=Yes)', 'type': 'Boolean'},
        {'name': 'Diverted', 'description': 'Diverted Flight Indicator (1=Yes)', 'type': 'Boolean'},
        {'name': 'DepTime', 'description': 'Actual Departure Time (local time: hhmm)', 'type': 'Datetime'},
        {'name': 'DepDelayMinutes','description': 'Difference in minutes between scheduled and actual departure time. Early departures set to 0.', 'type': 'Numeric'},
        {'name': 'DepDelay', 'description': 'Difference in minutes between scheduled and actual departure time. Early departures show negative numbers.', 'type': 'Numeric'},
        {'name': 'ArrTime', 'description': 'Actual Arrival Time (local time: hhmm)', 'type': 'Datetime'},
        {'name': 'ArrDelayMinutes', 'description': 'Difference in minutes between scheduled and actual arrival time. Early arrivals set to 0.', 'type': 'Numeric'},
        {'name': 'AirTime', 'description': 'Flight Time, in Minutes', 'type': 'Numeric'},
        {'name': 'Distance', 'description': 'Distance between airports (miles)', 'type': 'Numeric'},
        {'name': 'Year', 'description': 'Year', 'type': 'Numeric'},
        {'name': 'Quarter', 'description': 'Quarter(1-4)', 'type': 'Numeric'},
        {'name': 'Month', 'description': 'Month', 'type': 'Numeric'},
        {'name': 'DayofMonth', 'description': 'Day of Month', 'type': 'Numeric'},
        {'name': 'DayOfWeek', 'description': 'Day of Week', 'type': 'Numeric'},
        {'name': 'Marketing_Airline_Network', 'description': 'Unique Marketing Carrier Code. When the same code has been used by multiple carriers, a numeric suffix is used for earlier users, for example, PA, PA(1), PA(2). Use this field for analysis across a range of years.', 'type': 'Numeric'},
        {'name': 'Operated_or_Branded_Code_Share_Partners', 'description':'Reporting Carrier Operated or Branded Code Share Partners' , 'type': 'Numeric'},
        {'name': 'DOT_ID_Marketing_Airline', 'description': 'An identification number assigned by US DOT to identify a unique airline (carrier). A unique airline (carrier) is defined as one holding and reporting under the same DOT certificate regardless of its Code, Name, or holding company/corporation.', 'type': 'Numeric'},
        {'name': 'IATA_Code_Marketing_Airline', 'description': 'Code assigned by IATA and commonly used to identify a carrier. As the same code may have been assigned to different carriers over time, the code is not always unique. For analysis, use the Unique Carrier Code.', 'type': 'Numeric'},
        {'name': 'Flight_Number_Marketing_Airline', 'description': 'Flight Number', 'type': 'Numeric'},
        {'name': 'Operating_Airline', 'description': 'Unique Carrier Code. When the same code has been used by multiple carriers, a numeric suffix is used for earlier users, for example, PA, PA(1), PA(2). Use this field for analysis across a range of years.', 'type': 'Numeric'},
        {'name': 'DOT_ID_Operating_Airline', 'description': 'An identification number assigned by US DOT to identify a unique airline (carrier). A unique airline (carrier) is defined as one holding and reporting under the same DOT certificate regardless of its Code, Name, or holding company/corporation.', 'type': 'Numeric'},
        {'name': 'IATA_Code_Operating_Airline', 'description': 'Code assigned by IATA and commonly used to identify a carrier. As the same code may have been assigned to different carriers over time, the code is not always unique. For analysis, use the Unique Carrier Code.', 'type': 'Numeric'},
        {'name': 'Tail_Number', 'description': 'Tail Number', 'type': 'Numeric'},
        {'name': 'Flight_Number_Operating_Airline', 'description': 'Flight Number', 'type': 'Numeric'},
        {'name': 'OriginAirportID', 'description': 'Origin Airport, Airport ID. An identification number assigned by US DOT to identify a unique airport. Use this field for airport analysis across a range of years because an airport can change its airport code and airport codes can be reused.', 'type': 'Numeric'},
        {'name': 'DestAirportID', 'description': 'Destination Airport, Airport ID. An identification number assigned by US DOT to identify a unique airport. Use this field for airport analysis across a range of years because an airport can change its airport code and airport codes can be reused.', 'type': 'Numeric'},
        {'name': 'WheelsOff', 'description': 'Wheels Off Time (local time: hhmm)', 'type': 'Numeric'},
        {'name': 'WheelsOn', 'description': 'Wheels On Time (local time: hhmm)', 'type': 'Numeric'},
        {'name': 'ArrDelay', 'description': 'Difference in minutes between scheduled and actual arrival time. Early arrivals show negative numbers.', 'type': 'Numeric'},
        {'name': 'DivAirportLandings', 'description': 'Number of Diverted Airport Landings', 'type': 'Numeric'},
        {'name': 'DestAirportSeqID', 'description': 'Destination Airport, Airport Sequence ID. An identification number assigned by US DOT to identify a unique airport at a given point of time. Airport attributes, such as airport name or coordinates, may change over time.', 'type': 'Numeric'},
        {'name': 'DestCityMarketID', 'description': 'Destination Airport, City Market ID. City Market ID is an identification number assigned by US DOT to identify a city market. Use this field to consolidate airports serving the same city market.', 'type': 'Numeric'},
        {'name': 'Dest', 'description': 'Destination Airport', 'type': 'String'},
        {'name': 'DestCityName', 'description': 'Destination Airport, City Name', 'type': 'String'},
        {'name': 'DestState', 'description': 'Destination Airport, State Code', 'type': 'String'},
        {'name': 'DestStateFips', 'description': 'Destination Airport, State Fips', 'type': 'Numeric'},
        {'name': 'DestStateName', 'description': 'Destination Airport, State Name', 'type': 'String'},
        {'name': 'DestWac', 'description': 'Destination Airport, World Area Code', 'type': 'Numeric'},
        {'name': 'OriginAirportSeqID', 'description': 'Origin Airport, Airport Sequence ID. An identification number assigned by US DOT to identify a unique airport at a given point of time. Airport attributes, such as airport name or coordinates, may change over time.', 'type': 'Numeric'},
        {'name': 'OriginCityMarketID', 'description': 'Origin Airport, City Market ID. City Market ID is an identification number assigned by US DOT to identify a city market. Use this field to consolidate airports serving the same city market.', 'type': 'Numeric'},
        {'name': 'Origin', 'description': 'Origin Airport', 'type': 'String'},
        {'name': 'OriginCityName', 'description': 'Origin Airport, City Name', 'type': 'String'},
        {'name': 'OriginState', 'description': 'Origin Airport, State Code', 'type': 'String'},
        {'name': 'OriginStateFips', 'description': 'Origin Airport, State Fips', 'type': 'Numeric'},
        {'name': 'OriginStateName', 'description': 'Origin Airport, State Name', 'type': 'String'},
        {'name': 'OriginWac', 'description': 'Origin Airport, World Area Code', 'type': 'Numeric'},
    ]
    col_dict = {}

    for i in range(len(columns)):
        col_dict[i+1] = columns[i]

    return col_dict, render_template('about-dataset.html')