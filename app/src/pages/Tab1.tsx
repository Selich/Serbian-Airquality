import {
  IonGrid,
  IonRow,
  IonCol,
  IonCardTitle,
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
  IonText
} from "@ionic/react";
import { book, build, colorFill, grid } from "ionicons/icons";
import React, { useState, useEffect } from "react";
import { images, flash, send } from "ionicons/icons";
import ProgressBar from "../components/CircularBar";

import "./Home.css";

import axios from "axios";

// TODO: Color for AQ
const colorArray = [
  "#77ee11",
  "#ed004f",
  "#00fcf0",
  "#d2fc00",
  "#7bff00",
  "#fa6900"
];

const Tab1: React.FunctionComponent = () => {
  const [url, setUrl] = useState("");
  const [pastData, setPastData] = useState({});
  const [futureData, setFutureData] = useState({});
  const [city, setCity] = useState("novisad");
  const [color, setColor] = useState("");
  const [progress, setProgress] = useState(0);
  const [currAQI, setCurrAQI] = useState(0);

  useEffect(() => {
    axios.get("/aqi/" + city).then(res => setPastData(res.data));
  }, [city]);

  const randomColor = () => {
    return colorArray[Math.floor(Math.random() * colorArray.length)];
  };

  const options = {
    size: 250,
    progress: 20,
    strokeWidth: 15,
    circleOneStroke: "#d9edfe",
    circleTwoStroke: colorArray[0]
  };

  const backgroundStyle = {
    backgroundColor: "green",
    fontSize: 22,
    fontWeight: 900
  };

  const chartOptions = {
    chart: {
      id: "basic-bar"
    },
    xaxis: {
      categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998]
    }
  };
  const series = [
    {
      name: "series-1",
      data: [20, 20, 30, 40, 20, 10, 20]
    }
  ];

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Novi Sad</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent color="good">
        <ProgressBar {...options} />
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

export default Tab1;
