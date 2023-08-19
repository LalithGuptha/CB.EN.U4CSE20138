import React from 'react';
import { useParams } from 'react-router-dom';

function SingleTrainPage() {
  const { trainNumber } = useParams();
  fetch(`http://20.244.56.144/train/trains/${trainNumber}`).then(response => response.json());

  // Render train details using fetched data
  return (
    <div>
      <h1>Train Details</h1>
      {/* Rendering the train details here*/}
    </div>
  );
}

export default SingleTrainPage;
