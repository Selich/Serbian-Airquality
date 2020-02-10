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
  const [data, setData] = useState({})

  useEffect(() => {
    fetchData(url).then(data => setData(data.data))
  }, []);


  return (
    <IonPage >
      <IonHeader>
        <IonToolbar>
          <IonTitle>grad</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent>
        <div className="master">
       <IonCardTitle className="aqi-score">45</IonCardTitle>
       <IonCardSubtitle className="aqi-city">Novi Sad</IonCardSubtitle>
        </div>
      </IonContent>
    </IonPage>
  );
};

export default Tab1;
