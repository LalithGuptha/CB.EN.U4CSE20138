import React from 'react';
import { Link } from 'react-router-dom';

function TrainCard({ train }) {
  return (
    <div className="train-card">
      <h2>{train.trainName}</h2>
      <p>Train Number: {train.trainNumber}</p>
      {/* Display other train details */}
      <Link to={`/train/${train.trainNumber}`}>View Details</Link>
    </div>
  );
}

export default TrainCard;
