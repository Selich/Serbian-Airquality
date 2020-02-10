import {
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonCardSubtitle,
  IonCardTitle,
  IonContent,
  IonHeader,
  IonIcon,
  IonItem,
  IonLabel,
  IonList,
  IonListHeader,
  IonPage,
  IonButton,
  IonTitle,
  IonToolbar
} from '@ionic/react';
import { book, build, colorFill, grid } from 'ionicons/icons';
import React ,{ useState, useEffect } from 'react';
import { images, flash, send } from 'ionicons/icons';

import './Tab1.css';

import axios from 'axios'

const fetchData = (url: string) => (
    axios.get(url).then(res => {
      console.log(res)
      return res.data;
    })
 )

const Tab1: React.FunctionComponent = () => {

  const [url, setUrl] = useState('')
  const [pastData, setPastData] = useState([])
  const [futureData, setFutureData] = useState([])
  const [city, setCity] = useState('novisad')


  useEffect(() => {
    axios.get('/aqi/' + city)
    .then(res => setPastData(res.data))
  }, [city]);


  return (
    <IonPage >
      <IonHeader>
        <IonToolbar>
          <IonTitle>{city}</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent>
        <div className="master">
          { pastData.forEach(row => {console.log(row);
          })
          }
        <IonCardTitle className="aqi-score">45</IonCardTitle>
        <IonCardSubtitle className="aqi-city">Novi Sad</IonCardSubtitle>
        </div>
      </IonContent>
    </IonPage>
  );
};

export default Tab1;
