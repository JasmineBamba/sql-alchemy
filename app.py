# Import the dependencies.
from flask import Flask, jsonify
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)



#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################


# Define the route to the homepage
@app.route("/")
def home():
    return (
        "Welcome to the Climate App! Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/start<br/>"
        "/api/v1.0/start/end"
    )



# ----------------------------------------------------------------------------------------



# Define the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    session = Session(engine)
    
    # Find the most recent date in the data set.
    date_query = session.query(measurement.date).order_by(measurement.date.desc()).first()
    current_date = date_query[0]
    most_recent_date = dt.strptime(current_date, '%Y-%m-%d').date()

    # Calculate the date one year from the last date in data set.
    one_year_ago = most_recent_date - relativedelta(months=12)
    
    # Perform a query to retrieve the data and precipitation scores
    data_precip_score = session.query(measurement.date, measurement.prcp).filter(measurement.date >= one_year_ago).all()

    
    # Convert the query results to a dictionary
    precipitation = {}
    for date, prcp in data_precip_score:
        precipitation[date] = prcp

 
    return jsonify(precipitation)



# ----------------------------------------------------------------------------------------



# Define the stations route
@app.route("/api/v1.0/stations")
def stations():
    
    session = Session(engine)
    
    # Design a query to find the most active station
    most_active_stations = session.query(measurement.station, func.count(measurement.station)).\
        group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()

    # Extract station names from the query result
    station_names = [station[0] for station in most_active_stations]

    return jsonify(station_names)



# ----------------------------------------------------------------------------------------


# Define the temperature observations route
@app.route("/api/v1.0/tobs")
def tobs():
    
    session = Session(engine)
    
    date_query = session.query(measurement.date).order_by(measurement.date.desc()).first()
    current_date = date_query[0]
    most_recent_date = dt.strptime(current_date, '%Y-%m-%d').date()

    # Calculate the date one year from the last date in data set.
    one_year_ago = most_recent_date - relativedelta(months=12)
    most_active_stations = session.query(measurement.station, func.count(measurement.station)).\
        group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()
    
    # Most active station ID
    most_active_station_ID = most_active_stations[0][0]
    
    # Query the last 12 months of temperature observation data for the most active station
    temp_observation = session.query(measurement.date, measurement.tobs).filter(measurement.station == most_active_station_ID).filter(measurement.date >= one_year_ago).all()

    # Convert the query result to a list of temperatures
    #temperature_data = [temp[0] for temp in temp_observation]
    temperature_data = [{"date": temp[0], "temperature": temp[1]} for temp in temp_observation]
    
    return jsonify(temperature_data)



# ----------------------------------------------------------------------------------------
 
    
@app.route("/api/v1.0/<start>")
def temperature_stats_start(start):
    
    session = Session(engine)
        
    query = session.query(measurement.date, func.min(measurement.tobs).label("TMIN"),
        func.max(measurement.tobs).label("TMAX"),
        func.avg(measurement.tobs).label("TAVG")
    ).filter(measurement.date >= start).all()

    
    temperature_stats = []
    for row in query:
        temperature_data = {
            'Date': row.date,
            'Min Temp': row.TMIN, 
            'Max Temp': row.TMAX,
            'Average Temp': row.TAVG
        }
    temperature_stats.append(temperature_data)
   
    return jsonify(temperature_stats)

   


# ----------------------------------------------------------------------------------------


@app.route("/api/v1.0/<start>/<end>")
def temperature_stats_start_end(start, end):
    
    session = Session(engine)
   
    # Query the database to calculate TMIN, TAVG, and TMAX for dates within the specified date range
    results = session.query(measurement.date,
            func.min(measurement.tobs).label("TMIN"),
            func.max(measurement.tobs).label("TMAX"),
            func.avg(measurement.tobs).label("TAVG")
        ).filter(measurement.date >= start).filter(measurement.date <= end).all()
    
    
    temperature_stats = []
    for row in results:
        temperature_data = {
            'Date': row.date,
            'Min Temp': row.TMIN, 
            'Max Temp': row.TMAX,
            'Average Temp': row.TAVG
        }
    temperature_stats.append(temperature_data)
   
    return jsonify(temperature_stats)




if __name__ == "__main__":
    app.run(debug=True)