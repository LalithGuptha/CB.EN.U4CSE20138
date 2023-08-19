import logo from './logo.svg';
import './App.css';
 import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import AllTrainsPage from './pages/AllTrainsPage';
import SingleTrainPage from './pages/SingleTrainPage';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={AllTrainsPage} />
        <Route path="/train/:trainNumber" component={SingleTrainPage} />
      </Switch>
    </Router>
  );
}

export default App;
