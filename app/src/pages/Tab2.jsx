import React, { useState, useEffect } from "react";
import {
  IonGrid,
  IonCol,
  IonRow,
  IonText,
  IonContent,
  IonHeader,
  IonItem,
  IonLabel,
  IonList,
  IonPage,
  IonTitle,
  IonToolbar
} from "@ionic/react";

import axios from "axios";
import { Line } from "react-chartjs-2";
import "./Home.css";

const data = {
  labels: ["January", "February", "March", "April", "May", "June", "July"],
  datasets: [
    {
      label: "Predicted value of AQI",
      fill: true,
      lineTension: 0.2,
      backgroundColor: "rgba(75,192,192,0.4)",
      borderColor: "rgba(75,192,192,1)",
      borderCapStyle: "butt",
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: "miter",
      pointBorderColor: "rgba(75,192,192,1)",
      pointBackgroundColor: "#fff",
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(75,192,192,1)",
      pointHoverBorderColor: "rgba(220,220,220,1)",
      pointHoverBorderWidth: 2,
      pointRadius: 2,
      pointHitRadius: 10,
      data: [65, 59, 80, 81, 56, 55, 40]
    }
  ]
};
const Tab2 = () => {
  const [data, setData] = useState([]);
  const [city, setCity] = useState("novisad");

  useEffect(() => {
    axios.get("/prediction/" + city + "/7").then(res => setData(res.data));
    console.log(data);
  }, [city]);

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Prediction</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent color="good">
        <Line data={data} title="My amazing data" color="#70CAD1" />
        <IonGrid>
          <IonRow>
            <IonCol>
              <IonText color="text">O3: 35.36</IonText>
            </IonCol>
            <IonCol>
              <IonText color="text">NO2: 21.23</IonText>
            </IonCol>
            <IonCol>
              <IonText color="text">NOX: 31.44</IonText>
            </IonCol>
          </IonRow>
          <IonRow>
            <IonCol>
              <IonText color="text">CO: 6.67</IonText>
            </IonCol>
            <IonCol>
              <IonText color="text">NO: 17.04</IonText>
            </IonCol>
            <IonCol>
              <IonText color="text">PM1: 93.992</IonText>
            </IonCol>
          </IonRow>
        </IonGrid>
      </IonContent>
    </IonPage>
  );
};

export default Tab2;

