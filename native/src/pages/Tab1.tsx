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
  const [data, setData] = useState('')

  useEffect(() => {
    fetchData(url).then(data => setData(data.data))
  }, []);


  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Novi Sad</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent>
        <IonCard className="welcome-card aqi-card">
          <IonCardHeader>
            <IonCardTitle className="aqi-score">45</IonCardTitle>
            <IonCardSubtitle className="aqi-city">Novi Sad</IonCardSubtitle>
          </IonCardHeader>
          <IonCardContent className="aqi-content">
            <p>
              Now that your app has been created, you'll want to start building out features and
              components. Check out some of the resources below for next steps.
            </p>
          </IonCardContent>
        </IonCard>

        <IonList lines="none">
          <IonListHeader>
            <IonLabel>Resources</IonLabel>
          </IonListHeader>
          <IonItem href="https://ionicframework.com/docs/theming/basics" target="_blank">
            <IonIcon slot="start" color="medium" icon={colorFill} />
            <IonLabel>Theme Your App</IonLabel>
          </IonItem>
        </IonList>
      </IonContent>
    </IonPage>
  );
};

export default Tab1;
