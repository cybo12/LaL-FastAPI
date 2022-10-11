
import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    vus: 50,
  };

export default function () {
  http.get('http://lab1.gologic.ca:5001/pi/500');
  //sleep(1);
}