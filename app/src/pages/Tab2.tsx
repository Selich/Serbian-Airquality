import React from 'react';
import { IonGrid, IonCol, IonRow, IonText, IonContent, IonHeader, IonItem, IonLabel, IonList, IonPage, IonTitle, IonToolbar } from '@ionic/react';
import "./Home.css";
const data = [{name: 'Page A', uv: 400, pv: 2400, amt: 2400}];

const Tab2: React.FC = () => {
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Prediction</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent color="good">
      </IonContent>
    </IonPage>
  );
};

export default Tab2;