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
  labels: [
    "27.11.",
    "28.11.",
    "29.11.",
    "30.11.",
    "01.12.",
    "02.12.",
    "03.12."
  ],
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
      color: "rgba(0,0,0,1)",
      zeroLineColor: "white",
      pointHoverBorderWidth: 2,
      pointRadius: 2,
      pointHitRadius: 10,
      data: [
        17,
        17,
        16,
        18,
        20,
        17,
        18,
        16,
        15,
        15,
        16,
        19,
        19,
        19,
        19,
        18,
        18,
        19,
        20,
        19,
        23,
        25,
        24,
        19,
        17,
        17,
        16,
        17,
        20,
        22,
        21,
        22,
        21,
        21,
        21,
        21,
        20,
        20,
        19,
        19,
        18,
        18,
        17,
        17,
        17,
        17,
        16,
        16,
        16,
        16,
        17,
        18,
        20,
        19,
        18,
        18,
        17,
        18,
        18,
        19,
        21,
        22
      ]
    }
  ]
};
const Tab2 = () => {
  const [city, setCity] = useState("novisad");
  const [futureData, setFutureData] = useState([]);

  useEffect(() => {
    axios.get("/prediction/" + city + "/14").then(res => {
      console.log(res.data);
      setFutureData(res.data);
    });
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
      </IonContent>
    </IonPage>
  );
};

export default Tab2;
