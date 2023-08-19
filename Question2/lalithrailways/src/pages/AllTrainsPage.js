import React, { useState, useEffect } from 'react';
import TrainCard from '../components/TrainCard';

function AllTrainsPage() {
  const [trains, setTrains] = useState([]);

  useEffect(() => {
    // Fetch data from backend API and set it to the 'trains' state
   data =  fetch('http://20.244.56.144/train/trains').then(response => response.json()).then(data => setTrains(data));
  }, []);

  return (
    <div>
      <h1>All Trains</h1>
      {trains.map((train) => (
        <TrainCard key={train.trainNumber} train={train} />
      ))}
    </div>
  );
}

export default AllTrainsPage;
